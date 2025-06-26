import pandas as pd
import io
import base64
import json
import markdown
from ai_logic import generate_kpi_summary, chat_with_llm 

def ingest_and_summarize_kpis(uploaded_file) -> tuple[pd.DataFrame | None, str | None, str | None]:
    """
    Ingests data from an uploaded file (CSV, Excel, JSON),
    attempts to create a DataFrame, and generates a descriptive summary.

    Args:
        uploaded_file (streamlit.runtime.uploaded_file_manager.UploadedFile):
            The file object uploaded via Streamlit's st.file_uploader.

    Returns:
        tuple[pd.DataFrame | None, str | None, str | None]:
            - pd.DataFrame if successful, else None.
            - A Markdown table of the DataFrame's description, or None.
            - An error message if ingestion fails, else None.
    """
    df = None
    kpi_description_markdown = None
    error_message = None

    try:
        file_extension = uploaded_file.name.split('.')[-1].lower()
        file_content = uploaded_file.getvalue()

        if file_extension == 'csv':
            df = pd.read_csv(io.StringIO(file_content.decode('utf-8')))
        elif file_extension in ['xls', 'xlsx']:
            df = pd.read_excel(io.BytesIO(file_content))
        elif file_extension == 'json':
            # Attempt to read JSON as a flat table; may need more complex parsing for nested JSON
            df = pd.read_json(io.StringIO(file_content.decode('utf-8')))
        else:
            error_message = "Unsupported file type. Please upload a CSV, Excel (.xls, .xlsx), or JSON file."
            return None, None, error_message

        if df is not None and not df.empty:
            # Perform a basic statistical description
            # Exclude non-numeric columns from describe for a cleaner summary
            numeric_df = df.select_dtypes(include=['number'])
            if not numeric_df.empty:
                kpi_description = numeric_df.describe().transpose()
                kpi_description_markdown = kpi_description.to_markdown()
            else:
                kpi_description_markdown = "No numerical data found for statistical summary."
        elif df is not None and df.empty:
            error_message = "Uploaded file is empty or contains no data."
            return None, None, error_message
            
    except Exception as e:
        error_message = f"Error ingesting or processing file: {e}"
        return None, None, error_message

    return df, kpi_description_markdown, None


def generate_report_and_insights(uploaded_file, output_format: str = "markdown") -> tuple[str, str | None, bool, str | None, pd.DataFrame | None]:
    """
    Orchestrates the ingestion, KPI summarization, AI generation, and download link creation.

    Args:
        uploaded_file (streamlit.runtime.uploaded_file_manager.UploadedFile):
            The file object uploaded via Streamlit.
        output_format (str): The desired output format ('markdown' or 'html').

    Returns:
        tuple[str, str | None, bool, str | None, pd.DataFrame | None]:
            - The generated KPI summary text (Markdown) or an error message.
            - A base64 encoded download link for the summary file (str) or None.
            - A boolean indicating if the operation was successful (True/False).
            - An error message (str) if the operation failed, else None.
            - The ingested Pandas DataFrame for visualization, or None.
    """
    if uploaded_file is None:
        return "", None, False, "Please upload a report file to get started.", None

    df_kpis = None
    kpi_description_markdown = None
    
    try:
        df_kpis, kpi_description_markdown, ingest_error = ingest_and_summarize_kpis(uploaded_file)
        
        if ingest_error:
            return "", None, False, f"Data Ingestion Error: {ingest_error}", None
        
        if df_kpis is None or df_kpis.empty:
             return "No data was successfully ingested or the file is empty.", None, True, None, None # Consider this a soft success if no data
        
        if kpi_description_markdown is None or "No numerical data" in kpi_description_markdown:
            summary_text = "No numerical KPIs found in the report to generate a detailed summary. Try uploading a report with numeric columns."
            # We'll still allow plotting if there are non-numeric columns that can be used for index, etc.
        else:
            summary_text = generate_kpi_summary(kpi_description_markdown)

        if not summary_text or summary_text.startswith("ERROR:"):
            return "", None, False, summary_text, df_kpis # Return df_kpis even on AI error

        download_filename_prefix = uploaded_file.name.split('.')[0]
        download_link = None
        mime_type = None
        output_content = summary_text

        if output_format == "markdown":
            download_filename = f"{download_filename_prefix}_kpi_summary.md"
            encoded_content = base64.b64encode(output_content.encode("utf-8")).decode()
            mime_type = "text/markdown"
            download_link = f'data:{mime_type};base64,{encoded_content}'
        elif output_format == "html":
            html_summary = markdown.markdown(output_content, extensions=['fenced_code', 'tables', 'nl2br'])
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>KPI Summary - {download_filename_prefix}</title>
                <style>
                    body {{ font-family: 'Inter', sans-serif; line-height: 1.6; margin: 20px; color: #333; }}
                    h1, h2, h3, h4, h5, h6 {{ font-family: 'Inter', sans-serif; color: #2E86C1; }}
                    h2 {{ border-bottom: 1px solid #eee; padding-bottom: 5px; margin-top: 30px; }}
                    pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
                    code {{ background-color: #f9f9f9; padding: 2px 4px; border-radius: 3px; font-family: monospace; }}
                    ul {{ list-style-type: disc; padding-left: 20px; }}
                    ol {{ padding-left: 20px; }}
                    ul li, ol li {{ margin-bottom: 5px; }}
                </style>
            </head>
            <body>
                {html_summary}
            </body>
            </html>
            """
            download_filename = f"{download_filename_prefix}_kpi_summary.html"
            encoded_content = base64.b64encode(html_content.encode("utf-8")).decode()
            mime_type = "text/html"
            download_link = f'data:{mime_type};base64,{encoded_content}'
        else:
            return summary_text, None, False, "Unsupported output format for download.", df_kpis

        return summary_text, download_link, True, None, df_kpis

    except Exception as e:
        return "", None, False, f"An unexpected error occurred during report processing: {e}", df_kpis