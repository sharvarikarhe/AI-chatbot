# AI Chatbot Agent with LangGraph, Streamlit, and FastAPI

A modular, locally-deployed AI chatbot powered by **Groq** and **OpenAI** LLMs, capable of answering user queries with optional real-time web search integration using **Tavily**.

## 🔧 Features

- Agent-based reasoning using **LangGraph** and **LangChain**
- Real-time responses from **Groq (LLaMA 3, Mixtral)** and **OpenAI GPT-4o-mini**
- Optional web search with **Tavily API**
- Clean and interactive UI using **Streamlit**
- Fast and scalable backend with **FastAPI**
- API key management via environment variables

## Tech Stack

- **LLMs**: Groq (LLaMA 3, Mixtral), OpenAI (GPT-4o-mini)
- **Frontend**: Streamlit
- **Backend**: FastAPI, Pydantic
- **Agent Framework**: LangGraph, LangChain
- **Web Search**: Tavily API

## How to Run

1. **Clone the repo**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate   # for Windows
```

3. **Install requirements**

```bash
pip install -r requirements.txt
```

4. **Set up your .env file with these keys:**

```env
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

5. **Run the backend**

```bash
python backend.py
```

6. **Run the frontend** (in a new terminal)

```bash
streamlit run frontend.py
```

🧪 Sample Prompt
“List 3 top-performing stocks this week with a brief analysis.”
