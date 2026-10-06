📈 InvestAI
AI-Powered Investment Allocator
Build a smarter path to your financial goals.

 
 
 
 
 
 
🌟 What is InvestAI?
InvestAI is an AI-powered investment-planning application built with
Streamlit, FastAPI, LangGraph, and Groq.
The application collects an investor profile based on:
- 👤 Age
- 🎯 Investment goal
- ⏳ Investment horizon
- 🛡️ Risk tolerance
It then sends the profile through an AI workflow that:
1. Generates an educational asset allocation across stocks, bonds,
   and cash.
2. Maps the allocation to diversified ETF ideas.
3. Presents the results through a modern Streamlit dashboard.
Note: InvestAI is an educational software project. It is not a
financial advisory service and does not provide guaranteed or
personalized investment advice.

✨ Highlights
  Feature                             Description
  🤖 AI Analysis                  Uses an LLM to analyze the supplied
                                      investment profile.
  📊 Smart Allocation             Generates an educational allocation
                                      across stocks, bonds, and cash.
  💼 ETF Suggestions              Maps the suggested allocation to
                                      diversified ETF options.
  🔗 LangGraph Workflow           Orchestrates the profile →
                                      allocation → recommendation
                                      pipeline.
  ⚡ FastAPI Backend              Provides a clean API for
                                      investment-plan generation.
  🎨 Streamlit UI                 Provides the interactive InvestAI
                                      dashboard.
  🔐 Environment Secrets          Keeps the Groq API key outside the
                                  source code.
🧠 How It Works
                    INVESTAI
                       │
                       ▼
              ┌─────────────────┐
              │  Investor Input │
              │                 │
              │ Age             │
              │ Goal            │
              │ Horizon         │
              │ Risk            │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    FastAPI      │
              │    /allocate    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    LangGraph    │
              │     Workflow    │
              └────────┬────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      ┌─────────────┐     ┌───────────────┐
      │ Allocation  │────▶│ ETF Ideas     │
      │   Node      │     │     Node      │
      └─────────────┘     └───────────────┘
             │                   │
             └─────────┬─────────┘
                       ▼
                ┌─────────────┐
                │   Groq LLM  │
                └──────┬──────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Investment Plan │
              │                 │
              │ Allocation      │
              │ ETF Suggestions │
              └─────────────────┘
Workflow
Profile
   ↓
Allocation
   ↓
ETF Recommendations
   ↓
Investment Plan
🏗️ Architecture
┌──────────────────────────────────────────────┐
│                Streamlit UI                 │
│             streamlit_app.py                │
└──────────────────────┬───────────────────────┘
                       │
                       │ HTTP POST
                       ▼
┌──────────────────────────────────────────────┐
│                FastAPI Backend               │
│                   app.py                     │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                  LangGraph                   │
│                                              │
│  collector → suggest_allocation → recommend  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                  ChatGroq                    │
│              Configured LLM                  │
└──────────────────────────────────────────────┘
📁 Project Structure
InvestAI/
│
├── assets/
│   └── investai-growth.svg
│
├── app.py
├── collector.py
├── config.py
├── recommend.py
├── suggest.py
├── streamlit_app.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env                    # Local only — never commit
File Responsibilities
  File                           Purpose
  streamlit_app.py             Main Streamlit frontend and dashboard
  app.py                       FastAPI backend and LangGraph workflow
  collector.py                 Handles the investment-profile state
  suggest.py                   Generates the asset-allocation result
  recommend.py                 Generates ETF suggestions from the allocation
  config.py                    Loads environment variables and initializes ChatGroq
  requirements.txt             Python package dependencies
  assets/investai-growth.svg   InvestAI logo
  .gitignore                   Prevents secrets and local files from being committed
🛠️ Tech Stack
Frontend
- Streamlit
- Custom CSS
- Responsive dashboard UI
- HTTP communication with FastAPI
Backend
- FastAPI
- Pydantic
- Uvicorn
AI / Agent Workflow
- LangGraph
- LangChain Core
- ChatGroq
- Prompt-based asset allocation
- Prompt-based ETF recommendations
Configuration
- python-dotenv
- .env environment variables
⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/InvestAI.git
cd InvestAI
Replace YOUR_USERNAME with your GitHub username.
2. Create a virtual environment
Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
Windows CMD
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
🔑 Environment Variables
Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=your_groq_model_name
For example:
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
MODEL_NAME=openai/gpt-oss-120b
🔒 Keep your API key private
Never commit .env to GitHub.
Your repository should contain:
.env.example
instead of your real .env.
A safe example file can contain:
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=your_groq_model_name
▶️ Run the Application
InvestAI uses two processes: a FastAPI backend and a Streamlit
frontend.
Terminal 1 --- FastAPI
uvicorn app:app --port 8001
Backend:
http://127.0.0.1:8001
API documentation:
http://127.0.0.1:8001/docs
Terminal 2 --- Streamlit
Activate the virtual environment again if necessary:
.\venv\Scripts\Activate.ps1
Then:
streamlit run streamlit_app.py --server.port 8502
Open:
http://localhost:8502
🔌 API Reference
Health Check
GET
/
Response:
{
  "message": "InvestAI Investment Allocator is running"
}
Generate Investment Plan
POST
/allocate
Request:
{
  "age": 30,
  "goal": "retirement",
  "horizon": 25,
  "risk": "medium"
}
Response:
{
  "profile": {
    "age": 30,
    "goal": "retirement",
    "horizon": 25,
    "risk": "medium"
  },
  "allocation": "...",
  "recommendations": "..."
}
📊 Example Workflow
Input
Age:               30
Investment Goal:   Retirement
Investment Horizon: 25 years
Risk Tolerance:    Medium
AI Processing
Investor Profile
       ↓
LangGraph
       ↓
Asset Allocation
       ↓
ETF Mapping
       ↓
Final Investment Plan
Output
The application presents:
- 📊 Suggested stock allocation
- 🏦 Suggested bond allocation
- 💵 Suggested cash allocation
- 📈 ETF ideas
- 💰 Approximate expense ratios when available
- 📝 Short educational explanations
🔐 Security
Before pushing the project to GitHub:
- ❌ Never commit .env
- ❌ Never commit your Groq API key
- ❌ Never commit venv/
- ❌ Never commit __pycache__/
- ✅ Use environment variables
- ✅ Keep .gitignore enabled
- ✅ Use .env.example for public configuration documentation
If an API key is accidentally pushed to GitHub, revoke/rotate it
immediately.
⚠️ Limitations
InvestAI is currently an educational demonstration application.
The project:
- Does not execute trades.
- Does not connect to brokerage accounts.
- Does not manage real portfolios.
- Does not guarantee investment returns.
- Does not use the generated output as professional financial advice.
- Uses an LLM to generate ETF ideas rather than a dedicated live
  market-data provider.
- May produce approximate ETF expense-ratio information depending on
  the model's available knowledge.
🚀 Future Improvements
- [ ] Live market and ETF data
- [ ] Historical portfolio backtesting
- [ ] Portfolio performance charts
- [ ] Risk-score visualization
- [ ] User authentication
- [ ] Database integration
- [ ] Downloadable investment reports
- [ ] Docker deployment
- [ ] Cloud deployment
- [ ] Automated tests
- [ ] GitHub Actions CI/CD
- [ ] Portfolio comparison
- [ ] More asset classes
- [ ] Live ETF expense-ratio verification
- [ ] Improved recommendation evaluation
🎓 What This Project Demonstrates
This project demonstrates practical experience with:
- Python
- FastAPI
- Streamlit
- REST APIs
- Pydantic
- LangGraph
- LangChain
- LLM integration
- Groq API
- Prompt engineering
- Agent-style workflows
- State-based processing
- Frontend/backend integration
- Environment-variable management
- Git and GitHub
👨‍💻 Author
Krushna Chandra Bindhani
B.Tech Computer Science & Engineering
AI/ML • Data Science • Generative AI • LLM • Python
⭐ Support
If you find InvestAI useful or interesting:
- ⭐ Star the repository
- 🍴 Fork the project
- 🐛 Open an issue
- 💡 Suggest an improvement
⚖️ Disclaimer
InvestAI is an educational software project and demonstration of AI
application development.
The allocations and ETF ideas generated by the application are
produced by an AI model and may be incomplete, inaccurate, outdated,
or unsuitable for a particular individual.
This project does not provide personalized financial advice,
investment guarantees, or recommendations from a licensed financial
advisor.
Always perform independent research and consult a qualified financial
professional before making investment decisions.

📌 Project Status
Status: 🟢 Active Development
Application: InvestAI
Purpose: AI-powered educational investment planning
Architecture: Streamlit + FastAPI + LangGraph + Groq
💙 InvestAI
Smart Investments, Brighter Futures.