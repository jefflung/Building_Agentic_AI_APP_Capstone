"""
Fake News Detection System — powered by LangGraph + gpt-4o-mini (OpenAI)
"""

from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage, AIMessageChunk
from fake_news_agent.agent import fake_news_agent_graph

import re

def is_url(text):
    return text.startswith("http://") or text.startswith("https://")

BANNER = """
╔══════════════════════════════════════════════════════╗
║        Fake News Detection System (LangGraph)        ║
╚══════════════════════════════════════════════════════╝

This system analyzes the credibility of scientific or
technological content using an agent-based approach. 
It supports automated content retrieval for online articles.

You can input:
• Plain text (e.g. claims, short articles)
• Article URLs (the system will fetch and analyze content)

Examples:
  • This drug will cure cancer instantly
  • AI will replace all doctors in the future
  • https://example.com/article

Type 'quit' to exit.
"""


def run():
    print(BANNER)
    history = []

    MAX_INPUT_LENGTH = 2000  # safe limit

    while True:
        
        print("\nPaste your article (press ENTER twice to submit):")

        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)

        user_input = "\n".join(lines).strip()

        if len(user_input) > MAX_INPUT_LENGTH:
            print("\n⚠️ Input too long. Truncating for analysis...\n")
            user_input = user_input[:MAX_INPUT_LENGTH]

        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break

        if is_url(user_input):
            wrapped_input = f"Analyze the following article URL as a whole:\n\n{user_input}"
        else:
            wrapped_input = f"Analyze the following article as a whole:\n\n{user_input}"
        
        history.append(HumanMessage(content=wrapped_input))

        print("\nAgent: ", end="", flush=True)

        final_messages = None

        for event_type, data in fake_news_agent_graph.stream(
            {"messages": history},
            stream_mode=["messages", "values"],
            config={"recursion_limit": 10},
        ):
            if event_type == "messages":
                chunk, _ = data
                if isinstance(chunk, AIMessageChunk) and chunk.content:
                    print(chunk.content, end="", flush=True)
            elif event_type == "values":
                final_messages = data.get("messages", [])

        print()

        if final_messages:
            history = final_messages



if __name__ == "__main__":
    run()