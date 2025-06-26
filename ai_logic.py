import google.generativeai as genai
import os
from dotenv import load_dotenv
import pandas as pd

def _get_suitable_model(model_type: str = "text_generation"):
    """
    Finds and returns a suitable GenerativeModel that supports the specified model_type.
    Prioritizes 'gemini-1.5-flash-latest' or 'gemini-1.0-pro' for text generation.
    """
    try:
        available_models = genai.list_models()
        
        supported_models_names = []
        for m in available_models:
            if hasattr(m, 'supported_generation_methods') and 'generateContent' in m.supported_generation_methods:
                supported_models_names.append(m.name)

        # Prioritize specific models known to be good for text generation
        # Ensure we remove the 'models/' prefix when using them with GenerativeModel
        if 'models/gemini-1.5-flash-latest' in supported_models_names:
            return 'gemini-1.5-flash-latest'
        elif 'models/gemini-1.0-pro' in supported_models_names:
            return 'gemini-1.0-pro'
        elif 'models/gemini-pro' in supported_models_names: # Fallback to the original 'gemini-pro'
            return 'gemini-pro'
        elif supported_models_names: # If specific models not found, take the first suitable one
            # Basic heuristic: prefer models not just for embeddings or specific vision tasks
            for model_name in supported_models_names:
                if 'embedding' not in model_name and 'aqa' not in model_name:
                    return model_name.replace('models/', '') # Remove 'models/' prefix
            raise ValueError("No suitable text generation model found that supports generateContent after filtering.")
        else:
            raise ValueError("No models found that support generateContent.")

    except Exception as e:
        raise ConnectionError(f"Failed to list or select a suitable Generative AI model: {e}")

def _configure_genai():
    """Configures the Google Generative AI client with the API key."""
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY is not set in your .env file.")
    
    genai.configure(api_key=GOOGLE_API_KEY)


def generate_kpi_summary(kpi_data_markdown: str) -> str:
    """
    Analyzes provided KPI data (as Markdown table) using Google's Generative AI
    and generates a natural-language summary, highlighting trends, spikes, and anomalies.

    Args:
        kpi_data_markdown (str): A string containing KPI data, formatted as a Markdown table.

    Returns:
        str: A concise, plain English summary of KPIs, or an error message.
    """
    try:
        _configure_genai()
        model_name = _get_suitable_model()
        model = genai.GenerativeModel(model_name)
        print(f"DEBUG: KPI Summary - Using model: {model_name}")
    except Exception as e:
        return f"ERROR: Could not initialize Generative Model for KPI summary: {e}"

    prompt = f"""
    You are a Business Intelligence Analyst. Your task is to analyze the following business KPI data
    and provide a concise, natural-language summary. Highlight key trends, spikes, and anomalies.
    Keep the summary professional and actionable for decision-makers.

    ---
    KPI Data:
    {kpi_data_markdown}
    ---

    Provide your summary focusing on:
    - Overall performance across key metrics (e.g., Revenue, Churn, Conversion).
    - Significant increases or decreases (spikes/dips).
    - Emerging trends.
    - Any outliers or unusual data points.
    - Potential implications or areas for further investigation.

    Format your output clearly with bullet points or a coherent paragraph structure.
    """

    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=0.2)
        )
        if response and response.parts:
            return response.text
        elif response and response.candidates and response.candidates[0].text:
            return response.candidates[0].text
        else:
            return "AI response structure not as expected for KPI summary. Could not extract text."
    except Exception as e:
        print(f"DEBUG: Error during LLM API call for KPI summary: {e}")
        return f"ERROR: An error occurred while calling the Google Generative AI API for KPI summary: {e}"


def chat_with_llm(context_data_markdown: str, user_query: str, chat_history: list) -> str:
    """
    Responds to a user query in a conversational manner based on provided KPI data.

    Args:
        context_data_markdown (str): The KPI data or summary context for the chatbot, as a Markdown table.
        user_query (str): The user's question or prompt.
        chat_history (list): A list of previous messages in the chat, for context.
                             Each item is a dict: {"role": "user" or "model", "parts": [text]}

    Returns:
        str: The LLM's conversational response.
    """
    try:
        _configure_genai()
        model_name = _get_suitable_model()
        model = genai.GenerativeModel(model_name)
        print(f"DEBUG: Chatbot - Using model: {model_name}")
    except Exception as e:
        return f"ERROR: Could not initialize Generative Model for chatbot: {e}"

    # Prepare chat history for the model
    # The first message sets the context/system instruction
    initial_message = {
        "role": "user",
        "parts": [
            f"You are a helpful Business Intelligence chatbot. You are provided with business KPI data below. "
            f"Answer questions about this data naturally and concisely. If the question is outside the scope "
            f"of the provided data or general business knowledge, state that you cannot answer.\n\n"
            f"--- KPI Data Context ---\n{context_data_markdown}\n--- End KPI Data Context ---"
        ]
    }
    
    # Format existing chat history to fit Gemini's message structure
    formatted_history = []
    if chat_history:
        # Assuming chat_history is a list of {'role': 'user'/'assistant', 'content': 'text'}
        # Convert to {'role': 'user'/'model', 'parts': [text]}
        for msg in chat_history:
            role = "user" if msg["role"] == "user" else "model" # Gemini uses 'model' for its responses
            formatted_history.append({"role": role, "parts": [msg["content"]]})

    # Start a chat session with the model and provide the initial context and history
    chat = model.start_chat(history=[initial_message] + formatted_history)

    try:
        response = chat.send_message(user_query)
        if response and response.parts:
            return response.text
        elif response and response.candidates and response.candidates[0].text:
            return response.candidates[0].text
        else:
            return "AI chatbot response structure not as expected. Could not extract text."
    except Exception as e:
        print(f"DEBUG: Error during LLM API call for chatbot: {e}")
        return f"ERROR: An error occurred while calling the Google Generative AI API for chatbot: {e}"


# --- Example Usage (for local testing of ai_logic.py) ---
if __name__ == "__main__":
    print("--- Testing AI Logic for KPI Analyzer (ensure GOOGLE_API_KEY is set in .env) ---")

    # Dummy KPI data as a Markdown table
    dummy_kpi_data = """
| Metric           | Jan 2024 | Feb 2024 | Mar 2024 |
|:-----------------|:---------|:---------|:---------|
| Revenue ($)      | 100000   | 110000   | 130000   |
| Churn Rate (%)   | 5.0      | 5.5      | 6.0      |
| Conversion Rate (%) | 2.5      | 2.8      | 3.1      |
| New Customers    | 500      | 550      | 700      |
"""

    print("\n--- Generating KPI Summary ---")
    summary = generate_kpi_summary(dummy_kpi_data)
    print(summary)

    print("\n--- Testing Chatbot ---")
    chat_history_example = []
    query1 = "What are the main trends I should be aware of?"
    response1 = chat_with_llm(dummy_kpi_data, query1, chat_history_example)
    print(f"User: {query1}\nBot: {response1}")
    chat_history_example.append({"role": "user", "content": query1})
    chat_history_example.append({"role": "model", "content": response1})

    query2 = "Tell me more about the revenue trend."
    response2 = chat_with_llm(dummy_kpi_data, query2, chat_history_example)
    print(f"User: {query2}\nBot: {response2}")