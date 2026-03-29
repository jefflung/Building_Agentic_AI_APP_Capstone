from fastapi import FastAPI
from pydantic import BaseModel

from langchain_core.messages import HumanMessage
from fake_news_agent.agent import fake_news_agent_graph

app = FastAPI(
    title="Fake News Detection API",
    description="Agentic AI system for credibility analysis",
)

MAX_INPUT_LENGTH = 2000

# Request schema
class RequestBody(BaseModel):
    text: str

# Simple URL detection
def is_url(text: str) -> bool:
    return text.startswith("http://") or text.startswith("https://")


@app.get("/")
def root():
    return {"message": "Fake News Detection API is running"}

@app.post("/analyze")
def analyze(req: RequestBody):
    user_input = req.text.strip()

    if len(user_input) > MAX_INPUT_LENGTH:
        user_input = user_input[:MAX_INPUT_LENGTH]

    # Handle URL input
    if is_url(user_input):
        wrapped_input = f"Analyze the following article URL as a whole:\n\n{user_input}"
    else:
        wrapped_input = f"Analyze the following article as a whole:\n\n{user_input}"

    history = [HumanMessage(content=user_input)]

    final_messages = None

    for event_type, data in fake_news_agent_graph.stream(
        {"messages": history},
        stream_mode=["values"],
        config={"recursion_limit": 10},
    ):
        if event_type == "values":
            final_messages = data.get("messages", [])

    # Get final response
    if final_messages:
        last_message = final_messages[-1]
        return {
            "status": "success",
            "result": last_message.content
        }

    return {"status": "error", "result": "No response generated"}