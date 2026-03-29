# 🧠 Multi-Agent Fake News Detection System

A lightweight **agentic AI system** built using **LangGraph + FastAPI**, designed to evaluate the credibility of scientific and technological articles.

---

## 🚀 Features

* 🔍 **Claim Extraction** – identifies key statements from input text
* ⚖️ **Bias Detection** – detects exaggerated or misleading language
* 🚨 **Risk Classification** – evaluates misinformation risk
* 🌐 **Tool Integration** – includes a simple web search verification tool
* 🤖 **Agentic AI** – uses LangGraph ReAct agent pattern
* ☁️ **Cloud Deployment** – deployed on AWS Free Tier

---

## 🧱 System Architecture

User Input → LangGraph Agent → Tool Usage → Analysis → Output

The system uses a **ReAct-style agent** that dynamically decides when to call tools such as:

* Claim extraction
* Bias detection
* Risk classification
* Web search verification

---

## 📁 Project Structure

```
capstone/
│
├── fake_news_agent/
│   ├── agent.py
│   ├── tools/
│   │    └── analysis_tools.py
│   ├── config/
│   │    └── settings.py
│   └── .env
├── main.py
├── api.py
├── requirements.txt
├── Procfile           
├── .ebignore          
└── .ebextensions/
     └── python.config 
└── README.md
```

---

## ⚙️ Installation

### 1. Clone repository

```
git clone https://github.com/your-username/fake-news-agent.git
cd fake-news-agent
```

### 2. Create virtual environment

```
python -m venv venv
```

Activate:

* Windows: `venv\Scripts\activate`
* Mac/Linux: `source venv/bin/activate`

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run Locally

### Start API

```
uvicorn api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Request

```json
{
  "text": "This miracle drug will always cure cancer!"
}
```

---

## 📤 Example Response

```json
{
  "result": "The article contains exaggerated claims and shows high bias..."
}
```

---

## ☁️ AWS Deployment

This project is deployed using **AWS Elastic Beanstalk (Free Tier)**.

Steps:

```
eb init
eb create fake-news-agent-env
eb deploy
```

---

## ⚠️ Cost Note

To avoid charges:

```
eb terminate fake-news-agent-env
```

---

## 🎓 Academic Context

This project was developed as part of an **Agentic AI / LangGraph coursework assignment**, demonstrating:

* Multi-agent reasoning
* Tool integration
* API deployment
* Real-world application (content credibility analysis)

---

## 📌 Future Improvements

* Integrate real web search API (e.g. Tavily)
* Add database memory
* Improve NLP accuracy using LLM prompts
* Add evaluation metrics

---

## 👤 Author

Student Project — Building Agentic AI App course by Codecademy Nov 2025 - Mar 2026
(Company context anonymised)

---

## 📜 License

For academic use only.
