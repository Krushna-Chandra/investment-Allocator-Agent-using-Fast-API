# 📈 InvestAI

### AI-Powered Investment Allocation Assistant

> **Build a smarter path toward your financial goals with AI.**

InvestAI is an AI-powered educational investment-planning application that analyzes an investor profile and generates an **educational asset allocation** along with **diversified ETF ideas**.

Built with **Python, Streamlit, FastAPI, LangGraph, LangChain, and Groq**, InvestAI demonstrates how modern AI agent workflows can be integrated into a complete full-stack application.

---

## 🌟 Overview

InvestAI collects a simple investor profile:

- 👤 **Age**
- 🎯 **Investment Goal**
- ⏳ **Investment Horizon**
- 🛡️ **Risk Tolerance**

The profile is processed through an AI workflow that:

1. 🧠 Analyzes the investor profile
2. 📊 Generates an educational asset allocation
3. 💼 Maps the allocation to ETF ideas
4. 📝 Provides educational explanations
5. 🎨 Displays the results through an interactive Streamlit dashboard

> ⚠️ **Disclaimer:** InvestAI is an educational software project. It does not provide professional financial advice, guarantee investment returns, execute trades, or manage real portfolios.

---

# ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 **AI Analysis** | Uses an LLM to analyze the supplied investment profile |
| 📊 **Smart Allocation** | Generates educational allocations across stocks, bonds, and cash |
| 💼 **ETF Suggestions** | Maps suggested allocations to diversified ETF ideas |
| 🔗 **LangGraph Workflow** | Orchestrates the profile → allocation → recommendation pipeline |
| ⚡ **FastAPI Backend** | Provides a REST API for investment-plan generation |
| 🎨 **Streamlit Dashboard** | Interactive interface for entering profiles and viewing results |
| 🔐 **Secure Configuration** | Keeps API credentials outside the source code |
| 🧩 **Modular Architecture** | Separates collection, allocation, recommendations, configuration, and UI |

---

# 🧠 How InvestAI Works

```text
                    ┌─────────────────────┐
                    │       INVESTAI      │
                    │  AI Investment App  │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌─────────────────────────┐
                 │    Investor Profile     │
                 │                         │
                 │  • Age                  │
                 │  • Investment Goal      │
                 │  • Horizon              │
                 │  • Risk Tolerance       │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │       FastAPI           │
                 │       /allocate         │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │       LangGraph         │
                 │        Workflow         │
                 └────────────┬────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
          ┌─────────────────┐   ┌─────────────────┐
          │ Asset Allocation│   │   ETF Ideas     │
          │      Node       │   │      Node       │
          └────────┬────────┘   └────────┬────────┘
                   │                     │
                   └──────────┬──────────┘
                              ▼
                   ┌─────────────────────┐
                   │      Groq LLM       │
                   └──────────┬──────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │    Investment Plan      │
                 │                         │
                 │  • Allocation           │
                 │  • ETF Suggestions      │
                 │  • Explanations         │
                 └─────────────────────────┘
```

### 🔄 Workflow

```text
Investor Profile
       ↓
Collect Profile
       ↓
Asset Allocation
       ↓
ETF Recommendations
       ↓
Final Investment Plan
```

---

# 🏗️ System Architecture

```text
┌───────────────────────────────────────────────────────────┐
│                    Streamlit Frontend                     │
│                   streamlit_app.py                        │
└──────────────────────────┬────────────────────────────────┘
                           │
                           │ HTTP POST
                           ▼
┌───────────────────────────────────────────────────────────┐
│                     FastAPI Backend                       │
│                         app.py                            │
└──────────────────────────┬────────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────────┐
│                       LangGraph                           │
│                                                           │
│     collector → suggest_allocation → recommend            │
└──────────────────────────┬────────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────────┐
│                       ChatGroq                            │
│                    Configured LLM                         │
└───────────────────────────────────────────────────────────┘
```

---

# 📁 Project Structure

```text
investment-Allocator-Agent-using-Fast-API/
│
├── 📂 assets/
│   └── investai-growth.svg
│
├── 📄 app.py
├── 📄 collector.py
├── 📄 config.py
├── 📄 recommend.py
├── 📄 suggest.py
├── 📄 streamlit_app.py
│
├── 📄 requirements.txt
├── 📄 README.md
├── 📄 .gitignore
├── 📄 .env.example
└── 🔒 .env
```

> 🔒 `.env` is a local file and should never be committed to GitHub.

---

# 📌 File Responsibilities

| File | Responsibility |
|---|---|
| `streamlit_app.py` | Main Streamlit frontend and dashboard |
| `app.py` | FastAPI backend and LangGraph workflow |
| `collector.py` | Handles investment-profile state |
| `suggest.py` | Generates asset-allocation results |
| `recommend.py` | Generates ETF suggestions |
| `config.py` | Loads environment variables and initializes ChatGroq |
| `requirements.txt` | Python package dependencies |
| `assets/investai-growth.svg` | InvestAI branding asset |
| `.gitignore` | Prevents secrets and local files from being committed |
| `.env.example` | Example environment configuration |

---

# 🛠️ Technology Stack

## 🐍 Programming Language

- Python

## 🎨 Frontend

- Streamlit
- Custom CSS
- Interactive dashboard
- REST API communication

## ⚡ Backend

- FastAPI
- Pydantic
- Uvicorn

## 🧠 AI & Agent Workflow

- LangGraph
- LangChain Core
- ChatGroq
- Groq API
- Prompt Engineering
- LLM Integration
- State-based workflow

## ⚙️ Configuration

- python-dotenv
- Environment Variables
- `.env`

## 🔧 Development Tools

- VS Code
- Git
- GitHub
- Virtual Environment

---

# 🔄 Application Flow

```text
                    USER
                     │
                     ▼
          ┌─────────────────────┐
          │  Streamlit UI       │
          │                     │
          │ Age                 │
          │ Goal                │
          │ Horizon             │
          │ Risk                │
          └──────────┬──────────┘
                     │
                     │ POST /allocate
                     ▼
          ┌─────────────────────┐
          │     FastAPI         │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │     LangGraph       │
          └──────────┬──────────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
     Collector   Allocation  Recommend
                     │          │
                     └────┬─────┘
                          ▼
                    ┌───────────┐
                    │ Groq LLM  │
                    └─────┬─────┘
                          │
                          ▼
                 Investment Plan
                          │
                          ▼
                    Streamlit UI
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Krushna-Chandra/investment-Allocator-Agent-using-Fast-API.git
```

Move into the project directory:

```bash
cd investment-Allocator-Agent-using-Fast-API
```

---

## 2️⃣ Create a Virtual Environment

### Windows CMD

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Windows PowerShell

```bash
python -m venv venv
```

Activate it:

```bash
.\venv\Scripts\Activate.ps1
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=openai/gpt-oss-120b
```

### Example `.env.example`

Create a file named:

```text
.env.example
```

with:

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=your_groq_model_name
```

### 🔒 Important

Never upload your actual API key to GitHub.

Your `.gitignore` should include:

```gitignore
.env
.env.*
venv/
.venv/
__pycache__/
*.pyc
```

---

# ▶️ Run the Application

InvestAI uses two processes:

```text
┌─────────────────────┐
│   FastAPI Backend   │
│      Port 8001      │
└──────────┬──────────┘
           │
           │ HTTP
           ▼
┌─────────────────────┐
│ Streamlit Frontend  │
│      Port 8502      │
└─────────────────────┘
```

---

## 🖥️ Terminal 1 — Start FastAPI

Make sure your virtual environment is activated.

Run:

```bash
uvicorn app:app --port 8001
```

Backend:

```text
http://127.0.0.1:8001
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8001/docs
```

---

## 🎨 Terminal 2 — Start Streamlit

Activate the virtual environment:

```bash
.\venv\Scripts\Activate.ps1
```

Then run:

```bash
streamlit run streamlit_app.py --server.port 8502
```

Open the application in your browser:

```text
http://localhost:8502
```

---

# 🔌 API Reference

## 🟢 Health Check

### `GET /`

Returns the backend status.

### Example Response

```json
{
  "message": "InvestAI Investment Allocator is running"
}
```

---

## 📊 Generate Investment Plan

### `POST /allocate`

Generates an educational investment allocation and ETF recommendations based on the submitted investor profile.

### Request

```json
{
  "age": 30,
  "goal": "retirement",
  "horizon": 25,
  "risk": "medium"
}
```

### Response

```json
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
```

---

# 📊 Example Workflow

## 👤 Investor Profile

```text
Age:                30
Investment Goal:    Retirement
Investment Horizon: 25 years
Risk Tolerance:     Medium
```

## 🧠 AI Processing

```text
Investor Profile
       ↓
    LangGraph
       ↓
Asset Allocation
       ↓
   ETF Mapping
       ↓
Final Investment Plan
```

## 📈 Generated Output

The application presents:

- 📊 Suggested stock allocation
- 🏦 Suggested bond allocation
- 💵 Suggested cash allocation
- 📈 ETF ideas
- 💰 Approximate expense ratios when available
- 📝 Short educational explanations

---

# 🔐 Security

InvestAI follows basic environment-variable security practices.

### Never commit:

```text
❌ .env
❌ API Keys
❌ venv/
❌ __pycache__/
❌ *.pyc
```

### Recommended:

```text
✅ Environment variables
✅ .env.example
✅ .gitignore
✅ Secret rotation
```

If an API key is accidentally exposed on GitHub:

> **Immediately revoke or rotate the API key.**

---

# ⚠️ Limitations

InvestAI is currently an **educational AI demonstration application**.

The project:

- ❌ Does not execute trades
- ❌ Does not connect to brokerage accounts
- ❌ Does not manage real portfolios
- ❌ Does not guarantee investment returns
- ❌ Does not provide professional financial advice
- ⚠️ Uses an LLM to generate ETF ideas
- ⚠️ May produce approximate ETF expense-ratio information
- ⚠️ Does not currently use a dedicated live market-data provider

---

# 🚀 Future Improvements

## 📊 Data & Analytics

- [ ] Live market and ETF data
- [ ] Historical portfolio backtesting
- [ ] Portfolio performance charts
- [ ] Risk-score visualization
- [ ] Portfolio comparison
- [ ] More asset classes
- [ ] Live ETF expense-ratio verification

## 🤖 AI Improvements

- [ ] Improved recommendation evaluation
- [ ] Better portfolio reasoning
- [ ] More advanced risk analysis
- [ ] Improved prompt engineering
- [ ] AI-generated portfolio explanations

## 🔐 Application Features

- [ ] User authentication
- [ ] Database integration
- [ ] User portfolio history
- [ ] Downloadable investment reports

## ☁️ Deployment

- [ ] Docker deployment
- [ ] Cloud deployment
- [ ] Automated testing
- [ ] GitHub Actions CI/CD

---

# 🎓 What This Project Demonstrates

InvestAI demonstrates practical experience with:

```text
🐍 Python
⚡ FastAPI
🎨 Streamlit
🔌 REST APIs
📦 Pydantic

🧠 LangGraph
🔗 LangChain
🤖 LLM Integration
⚡ Groq API
✍️ Prompt Engineering

🔄 Agent-style Workflows
🧩 State-based Processing
🔗 Frontend / Backend Integration

🔐 Environment Variables
🌐 Git & GitHub
```

---

# 💡 Why InvestAI?

InvestAI demonstrates how an AI concept can be transformed into a complete application.

Instead of building only a simple LLM prompt, the project combines:

```text
              ┌──────────────┐
              │     AI       │
              └──────┬───────┘
                     │
                     ▼
            ┌─────────────────┐
            │ Agent Workflow  │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │    FastAPI      │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │    Streamlit    │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │   Git / GitHub  │
            └─────────────────┘
```

This makes InvestAI a practical demonstration of modern:

- Generative AI application development
- Agentic AI workflows
- Full-stack AI development
- API integration
- LLM application architecture

---

# 📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

- Building REST APIs using FastAPI
- Creating interactive applications with Streamlit
- Building state-based workflows with LangGraph
- Integrating Groq-hosted LLMs
- Working with LangChain
- Designing AI prompts
- Connecting frontend and backend applications
- Managing environment variables
- Structuring a modular Python application
- Using Git and GitHub for version control

---

# 👨‍💻 Author

## Krushna Chandra Bindhani

**B.Tech Computer Science & Engineering**

### Areas of Interest

```text
AI/ML
Data Science
Generative AI
LLM Applications
Python
FastAPI
LangChain
LangGraph
```

---

# ⭐ Support

If you find **InvestAI** useful or interesting:

⭐ **Star** the repository  
🍴 **Fork** the project  
🐛 **Open** an issue  
💡 **Suggest** an improvement  

### GitHub Repository

https://github.com/Krushna-Chandra/investment-Allocator-Agent-using-Fast-API

---

# ⚖️ Disclaimer

InvestAI is an **educational software project and AI application-development demonstration**.

The allocations and ETF ideas generated by the application are produced by an AI model and may be incomplete, inaccurate, outdated, or unsuitable for a particular individual.

This project does **not** provide:

- Personalized financial advice
- Investment guarantees
- Professional portfolio management
- Recommendations from a licensed financial advisor

Always perform independent research and consult a qualified financial professional before making investment decisions.

---

# 📌 Project Status

```text
🟢 ACTIVE DEVELOPMENT
```

| Category | Details |
|---|---|
| 🚀 Application | **InvestAI** |
| 🎯 Purpose | AI-powered educational investment planning |
| 🐍 Language | Python |
| 🎨 Frontend | Streamlit |
| ⚡ Backend | FastAPI |
| 🧠 Workflow | LangGraph |
| 🔗 Framework | LangChain |
| 🤖 LLM | Groq |
| 🌐 Repository | GitHub |

---

# 📈 InvestAI

### Smart Investments • Brighter Futures

Built with ❤️ using **Python • Streamlit • FastAPI • LangGraph • LangChain • Groq**

⭐ Star the repository if you like the project!
