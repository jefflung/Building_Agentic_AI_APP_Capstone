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
* * 🔗 **URL Analysis** – supports article links and extracts content automatically

---

## 🧱 System Architecture

User Input → FastAPI → LangGraph Agent → Tools → LLM → Structured Output

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
├── .ebextensions/
│    └── python.config 
└── README.md
```

---

## ⚙️ Installation

### 1. Clone repository

```
git clone https://github.com/jefflung/Building_Agentic_AI_APP_Capstone.git
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
  "result": "[Claims] ... [Bias] ... [Risk] ... [Conclusion] ..."
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
## 🌍 Live Demo

API Documentation:
http://fake-news-detector-env.eba-a2fd7933.eu-north-1.elasticbeanstalk.com/docs

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
 * 🔗 **URL Analysis** – supports article links and extracts content automatically

---

## 📦 Requirements

- Python 3.10+
- OpenAI API Key

---

## 🎬 Report and Video demo

Peport PDF : https://drive.google.com/file/d/1muFbm0ZIsGq69DiGpgZrVD8UAbmQvJWc/view?usp=drive_link

Video demo : https://drive.google.com/file/d/1FcZ690agxED5L1AWhkd3GgNpzOeoJRbu/view?usp=sharing


## 👤 Author

Student Project — Building Agentic AI App course by Codecademy Nov 2025 - Mar 2026
(Company context anonymised)

---

## 📜 License

For academic use only.
