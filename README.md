# 📈 LLM-Powered Business KPI Analyzer

## Overview

The **LLM-Powered Business KPI Analyzer** is an interactive Streamlit web application designed to empower decision-makers by transforming raw business report data (CSV, Excel, JSON) into actionable, natural-language insights. Leveraging the advanced capabilities of Google's Gemini Large Language Model, this tool automatically summarizes key performance indicators (KPIs), highlights critical trends, spikes, and anomalies, and provides a dynamic visual representation of your data.

Go beyond static dashboards. Upload your reports, get instant AI-driven analysis, visualize trends, and even chat with your data for deeper understanding!

## ✨ Features

* **AI-Powered KPI Summaries:**
    * Generates concise, natural-language summaries of your business KPIs (e.g., Revenue, Churn, Conversion Rate).
    * Automatically highlights significant trends, outliers, and performance drivers by leveraging Google's Gemini LLM.
    * Output is structured for readability, making it easy to grasp complex data points.

* **Interactive KPI Trend Visualization:**
    * Dynamically plots chosen numerical KPIs over time using `Plotly.express`.
    * Provides an interactive line chart to visualize trends, allowing users to zoom, pan, and hover for detailed insights.
    * Intelligently attempts to identify and use date/time columns for accurate time-series plotting.

* **Conversational AI Chatbot:**
    * Engage with your analyzed KPI data through a simple, yet powerful chatbot.
    * Ask natural language questions about trends, specific metrics, or comparisons, and get AI-generated answers based on the uploaded data.
    * Perfect for quick ad-hoc queries without needing to manipulate spreadsheets.

* **Flexible Data Ingestion:**
    * Supports various common business report formats: CSV, Excel (`.xls`, `.xlsx`), and JSON.
    * Robust parsing ensures that your data is correctly ingested and prepared for analysis.

* **Professional & Customizable UI:**
    * Features a sleek, modern dark-mode aesthetic by default, designed for optimal readability and a premium feel.
    * Includes a convenient toggle to switch between dark and light themes, catering to user preference.
    * Custom CSS ensures a polished user experience with refined input fields, buttons, and content presentation.

* **Downloadable Reports:**
    * Download the AI-generated KPI summary in either Markdown (`.md`) or HTML (`.html`) format for sharing, presentations, or record-keeping.

* **Robust LLM Integration:**
    * Automatically selects the most suitable available Google Gemini model (`gemini-1.5-flash-latest`, `gemini-1.0-pro`, or `gemini-pro`) to ensure optimal performance and accessibility.

## 🚀 How It Works

1.  **Upload Report:** Users upload their business report file (CSV, Excel, or JSON) via the Streamlit interface.
2.  **Data Ingestion & Summary:** The `features.py` module ingests the data using `pandas`, generates a statistical description of the numerical KPIs, and prepares it for the LLM.
3.  **AI Analysis:** The raw statistical summary (and relevant data for the chatbot) is sent to the Google Gemini LLM via `ai_logic.py`, which generates a natural-language business summary highlighting trends, anomalies, and actionable insights.
4.  **Interactive Visualization:** The ingested data is used to create a dynamic line graph showcasing KPI trends over time, providing a visual complement to the AI summary.
5.  **Chatbot Interaction:** Users can type questions into the chatbot, and the LLM provides contextual answers based on the uploaded data and its prior analysis.
6.  **Display & Download:** Both the AI-generated summary, the interactive graph, and the chatbot interface are presented in the web application. Users can also download the comprehensive AI summary report.

## 🛠️ Setup Instructions

Follow these steps to get the Business KPI Analyzer running on your local machine.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### 1. Clone the Repository

First, clone this repository to your local machine (replace `your-username/your-repo` with the actual path if hosted on GitHub):

```bash
git clone [https://github.com/your-username/llm-kpi-analyzer.git](https://github.com/your-username/llm-kpi-analyzer.git)
cd llm-kpi-analyzer
````

### 2\. Create a Virtual Environment (Recommended)

It's best practice to use a virtual environment to manage project dependencies and avoid conflicts:

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3\. Install Dependencies

Once your virtual environment is activated, install all necessary Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4\. Set Up Google Gemini API Key

This project requires a Google Gemini API Key to interact with the Large Language Model.

1.  **Obtain Your API Key:**

      * Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
      * Sign in with your Google account.
      * Follow the prompts to create a new API key. It's free for basic usage within generous limits.
      * **Copy the generated API key immediately.**

2.  **Create the `.env` File:**

      * In the **root directory of your project** (the same folder as `main.py`), create a new file named exactly: `.env` (ensure no extra file extension).

3.  **Add Your Key to `.env`:**

      * Open the `.env` file with a plain text editor.
      * Add the following line, replacing `"YOUR_API_KEY_HERE"` with the actual key you copied:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```
      * **Example:**
        ```
        GOOGLE_API_KEY="AIzaSyBXXXXXXXXXXXXXXXXXXXXXXX"
        ```

    **Security Note:** **Never commit your `.env` file to public version control systems (like GitHub)** as it contains sensitive credentials. It is already included in a standard `.gitignore` file for this purpose.

## 🚀 Running the Application

After completing the setup:

1.  Ensure your virtual environment is active.

2.  Navigate to the project's root directory in your terminal.

3.  Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

    Your default web browser should automatically open a new tab pointing to the application (usually `http://localhost:8501`). Keep the terminal window open as long as you want the application to run. To stop the application, press `Ctrl + C` in the terminal.

## 📂 Project Structure

```
llm-kpi-analyzer/
├── .env                     # Your Google Gemini API Key (private)
├── .gitignore               # Files to be ignored by Git
├── main.py                  # Main Streamlit application entry point
├── features.py              # Handles data ingestion, basic KPI summarization, and orchestration
├── ai_logic.py              # Manages Google Gemini API interaction and LLM prompting for both summary & chat
├── styling.py               # Custom CSS for professional UI and theme toggling
├── requirements.txt         # Lists all Python package dependencies
└── README.md                # This project's README file
```

## 🧪 Testing with Sample Data

To test the project, you can create a CSV file named `monthly_business_kpis.csv` in your project directory with the following content:

```csv
Date,Region,Product_Category,Monthly_Revenue,Monthly_Costs,New_Customers,Customer_Churn_Rate,Marketing_Spend,Conversion_Rate
2023-01-31,North,Electronics,150000,75000,1500,0.02,20000,0.05
2023-01-31,South,Apparel,80000,40000,800,0.03,10000,0.04
2023-01-31,East,Home Goods,120000,60000,1000,0.025,15000,0.06
2023-01-31,West,Electronics,180000,90000,1700,0.015,25000,0.055
2023-02-28,North,Electronics,155000,76000,1550,0.018,21000,0.052
2023-02-28,South,Apparel,82000,41000,810,0.028,10500,0.042
2023-02-28,East,Home Goods,125000,61000,1050,0.023,16000,0.061
2023-02-28,West,Electronics,185000,91000,1750,0.014,26000,0.057
2023-03-31,North,Electronics,160000,78000,1600,0.019,22000,0.053
2023-03-31,South,Apparel,85000,42000,830,0.027,11000,0.045
2023-03-31,East,Home Goods,130000,63000,1100,0.022,17000,0.063
2023-03-31,West,Electronics,190000,93000,1800,0.013,27000,0.058
2023-04-30,North,Electronics,162000,79000,1620,0.02,22500,0.054
2023-04-30,South,Apparel,83000,41500,800,0.03,10800,0.041
2023-04-30,East,Home Goods,132000,64000,1080,0.024,17500,0.062
2023-04-30,West,Electronics,192000,94000,1820,0.015,27500,0.059
2023-05-31,North,Electronics,165000,80000,1650,0.017,23000,0.055
2023-05-31,South,Apparel,86000,43000,840,0.029,11200,0.043
2023-05-31,East,Home Goods,135000,65000,1120,0.021,18000,0.064
2023-05-31,West,Electronics,195000,95000,1850,0.012,28000,0.06
2023-06-30,North,Electronics,168000,81000,1680,0.016,23500,0.056
2023-06-30,South,Apparel,88000,44000,860,0.026,11500,0.046
2023-06-30,East,Home Goods,138000,66000,1150,0.02,18500,0.065
2023-06-30,West,Electronics,198000,96000,1880,0.011,28500,0.061
```

Upload this `monthly_business_kpis.csv` file to the Streamlit app to observe the AI summary, the interactive KPI trend graph, and engage with the chatbot.

## 🔮 Future Enhancements

  * **Advanced Data Transformations:** Allow users to define custom calculations or aggregations (e.g., "Revenue per Customer").
  * **Previous Period Comparison:** Integrate functionality to compare current report data with a previous period for explicit MoM/QoQ analysis.
  * **Threshold-Based Flagging:** Implement user-defined rules (e.g., "flag churn \> 10%") to highlight specific KPI conditions in the summary.
  * **Automated Reporting:** Extend to auto-email KPI reports to stakeholders or integrate with BI dashboards for automated summary generation.
  * **Multilingual Support:** Add support for generating summaries and chatbot responses in multiple languages.
  * **Enhanced Visualization Options:** Offer more chart types (e.g., bar charts, pie charts) and customization options for the graphs.
  * **API Usage Monitoring:** Integrate token usage tracking to help users manage API costs.

## 🤝 Contributing

Contributions are welcome\! If you have ideas for improvements, bug fixes, or new features, please feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

  * **Google Gemini:** For providing the powerful large language model that drives the AI analysis.
  * **Streamlit:** For enabling rapid development of interactive web applications in Python.
  * **Pandas:** For robust data manipulation and analysis.
  * **Plotly:** For creating stunning interactive data visualizations.
