# InvestAI Investment Allocator

An educational investment-planning app that collects an investor profile, generates a suggested asset allocation, and provides diversified ETF ideas.

## Stack

- Streamlit user interface
- FastAPI backend
- LangGraph workflow
- Groq language model

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create a `.env` file:

   ```env
   GROQ_API_KEY=your_groq_api_key
   MODEL_NAME=your_groq_model_name
   ```

## Run locally

Start the FastAPI backend:

```powershell
uvicorn app:app --port 8001
```

In a second terminal, start Streamlit:

```powershell
streamlit run streamlit_app.py --server.port 8502
```

Open `http://localhost:8502` in your browser.

## Disclaimer

This project is for educational purposes only and does not provide personalized financial advice.
