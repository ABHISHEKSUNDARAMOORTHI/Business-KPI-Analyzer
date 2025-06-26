import streamlit as st
import os
from dotenv import load_dotenv
from styling import apply_base_styles # Changed to apply_base_styles
from features import generate_report_and_insights
from ai_logic import chat_with_llm
import pandas as pd
import plotly.express as px

def main():
    """
    Main function to run the Streamlit application for the Business KPI Analyzer.
    """
    st.set_page_config(
        page_title="LLM-Powered KPI Analyzer",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Theme toggle in sidebar
    with st.sidebar:
        dark_mode = st.toggle("Dark Mode", value=True, help="Toggle between dark and light themes.")
    
    apply_base_styles(dark_mode) # Pass the dark_mode preference to styling

    # Hero Section - using custom classes from styling.py
    st.markdown(f"""
    <div class="hero-section">
        <h1 class="hero-title"><i class="fas fa-chart-line"></i> Business KPI Analyzer</h1>
        <p class="hero-subtitle">Transforming Raw Data into Actionable Insights with Generative AI.</p>
        <p class="hero-tagline">Effortlessly understand trends, anomalies, and performance drivers.</p>
    </div>
    """, unsafe_allow_html=True)

    # Removed the st.title and st.markdown for the main description as they are now in the hero section.
    # The image also moves into the "get started" block.

    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    if not GOOGLE_API_KEY:
        st.error("🚨 Google Gemini API Key is not set! Please add `GOOGLE_API_KEY=\"YOUR_API_KEY\"` to your `.env` file.")
        st.stop()

    st.sidebar.header("Upload Your Report")
    uploaded_file = st.sidebar.file_uploader(
        "Choose a file",
        type=["csv", "xls", "xlsx", "json"],
        help="Upload your business report (CSV, Excel, or JSON)."
    )

    st.sidebar.header("Output Options")
    output_format = st.sidebar.radio(
        "Select Report Format:",
        ("Markdown", "HTML"),
        help="Choose the format for the downloadable KPI analysis report."
    ).lower()

    process_button = st.sidebar.button("Analyze Report", use_container_width=True, type="primary")

    st.markdown("---")

    # Initialize session state for chat history if not already present
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "df_kpis" not in st.session_state:
        st.session_state.df_kpis = None
    if "kpi_summary_text" not in st.session_state:
        st.session_state.kpi_summary_text = ""

    if uploaded_file is not None and process_button:
        with st.spinner("Analyzing report and generating insights... This might take a moment."):
            summary_text, download_link, success, error_message, df_kpis = generate_report_and_insights(uploaded_file, output_format)

            st.session_state.df_kpis = df_kpis
            st.session_state.kpi_summary_text = summary_text

            if success:
                st.success("KPI Analysis Complete!")
                
                st.subheader("💡 Business KPI Summary")
                st.markdown(summary_text)

                if df_kpis is not None and not df_kpis.empty:
                    numeric_cols = df_kpis.select_dtypes(include=['number']).columns.tolist()
                    
                    if not numeric_cols:
                        st.info("No numerical columns found in the report to generate a KPI trend graph.")
                    else:
                        st.markdown("---")
                        st.subheader("📊 KPI Trend Visualization")
                        
                        x_axis_col = None
                        for col in df_kpis.columns:
                            if "date" in col.lower() or "month" in col.lower() or "period" in col.lower() or "week" in col.lower():
                                try:
                                    df_kpis[col] = pd.to_datetime(df_kpis[col], errors='coerce')
                                    if df_kpis[col].notna().any():
                                        x_axis_col = col
                                        break
                                except:
                                    pass

                        if x_axis_col is None:
                            st.info("No clear date/time column detected. Plotting against row index. Ensure your report has a date column for better trend analysis.")
                            df_kpis['index'] = df_kpis.index
                            x_axis_col = 'index'


                        selected_kpi = st.selectbox(
                            "Select a KPI to visualize:",
                            options=numeric_cols,
                            key="kpi_select", # Added key for uniqueness
                            help="Choose a numerical KPI column from your report to plot its trend."
                        )

                        if selected_kpi:
                            df_plot = df_kpis.dropna(subset=[x_axis_col, selected_kpi]) if x_axis_col != 'index' else df_kpis.copy()
                            
                            if not df_plot.empty:
                                fig = px.line(
                                    df_plot,
                                    x=x_axis_col,
                                    y=selected_kpi,
                                    title=f'{selected_kpi} Trend Over Time',
                                    labels={x_axis_col: 'Time Period', selected_kpi: selected_kpi},
                                    markers=True,
                                    hover_data={x_axis_col: True, selected_kpi: True}
                                )
                                fig.update_xaxes(rangeslider_visible=True)
                                fig.update_layout(hovermode="x unified")
                                st.plotly_chart(fig, use_container_width=True)
                            else:
                                st.warning(f"No valid data points found for '{selected_kpi}' to plot after filtering for time periods.")
                else:
                    st.info("No numerical data found or DataFrame is empty to generate KPI trend graphs.")

                st.markdown("---")
                st.subheader("💬 Chat with your KPIs")
                st.info("Ask questions about your KPIs! The chatbot uses the analyzed data to respond.")

                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

                if prompt := st.chat_input("Ask a question about your KPIs...", key="chat_input"): # Added key
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    with st.chat_message("user"):
                        st.markdown(prompt)

                    with st.spinner("Thinking..."):
                        if st.session_state.df_kpis is not None and not st.session_state.df_kpis.empty:
                            context_for_chat = st.session_state.df_kpis.to_markdown(index=False)
                        else:
                            context_for_chat = st.session_state.kpi_summary_text

                        chatbot_response = chat_with_llm(context_for_chat, prompt, st.session_state.messages)
                        
                        st.session_state.messages.append({"role": "assistant", "content": chatbot_response})
                        with st.chat_message("assistant"):
                            st.markdown(chatbot_response)

                st.markdown("---")
                st.subheader("⬇️ Download Analysis Report")
                st.download_button(
                    label=f"Download {output_format.upper()} Report",
                    data=download_link,
                    file_name=uploaded_file.name.replace(".", "_") + f"_kpi_summary.{output_format}",
                    mime=f"text/{output_format}",
                    key="download_kpi_report_button",
                    help=f"Click to download the KPI analysis report as a .{output_format} file."
                )
                
            else:
                st.error(f"Failed to analyze report: {error_message}")
                if "API key" in error_message or "authentication" in error_message or "configure" in error_message:
                    st.warning("Ensure your Google Gemini API key is correctly set in the `.env` file and has sufficient permissions.")
                elif "UnicodeDecodeError" in error_message:
                    st.info("The file might be in a different encoding. Try converting it to UTF-8 or ensure it's plain text.")
                st.info("If the issue persists, check your internet connection or try a different report file.")

    elif uploaded_file is None and process_button:
        st.warning("Please upload a report file first before clicking 'Analyze Report'.")
        
    elif uploaded_file is None:
        st.info("Upload your business report on the left sidebar and click 'Analyze Report' to get started.")
        # Removed image from info block as Hero section replaces it
        # If you still want an image here, re-add st.image(...)

    # The new footer will automatically appear sticky at the bottom
    st.markdown(
        """
        <footer>
            <div style="text-align: center;">
                Developed with ❤️ for Data Engineers & Analysts. Powered by Google Gemini and Streamlit.
            </div>
        </footer>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()