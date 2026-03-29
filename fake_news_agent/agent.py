from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage
from langgraph.prebuilt import create_react_agent

from fake_news_agent.config.settings import (
    OPENAI_API_KEY,
    MODEL_NAME,
    TEMPERATURE
)

from fake_news_agent.tools.analysis_tools import (
    extract_claims,
    detect_bias,
    classify_risk,
    web_search_tool,
    fetch_article_from_url,
)

TOOLS = [
    fetch_article_from_url,
    extract_claims,
    detect_bias,
    classify_risk,
    web_search_tool,
]

SYSTEM_PROMPT = """You are a scientific article credibility analysis assistant.

Your tasks:
1. Extract key claims
2. Detect bias
3. Assess misinformation risk

Guidelines:
- Use tools step-by-step when needed
- Do not repeat tool calls unnecessarily
- Stop once sufficient analysis is completed
- Provide final answer clearly without looping
- Be concise and structured
- Always produce a single consolidated analysis, even if the input contains multiple paragraphs
- Perform ONE combined analysis, not separate analyses per paragraph
- Provide a single final structured output
- Output should contain only ONE set of:
  [Claims]
  [Bias]
  [Risk]
  [Conclusion]
"""

def _prompt(state: dict):
    return [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]


llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=MODEL_NAME,
    temperature=TEMPERATURE
)

fake_news_agent_graph = create_react_agent(
    model=llm,
    tools=TOOLS,
    prompt=_prompt
)