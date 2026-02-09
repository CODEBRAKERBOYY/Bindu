"""
Beginner Zero-Config Bindu Agent

Purpose:
- Help first-time users run Bindu locally in under 1 minute
- No database, Redis, or cloud dependencies
- Safe default agent for learning Bindu fundamentals
"""

from bindu.penguin.bindufy import bindufy
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file


agent = Agent(
    instructions="You are a friendly assistant that explains things simply.",
    model=OpenRouter(id="openai/gpt-oss-120b"),
    tools=[DuckDuckGoTools()],
)

config = {
    "author": "21uad051@kamarajengg.edu.in",
    "name": "beginner_zero_config_agent",
    "description": "Zero-config local Bindu agent for first-time users",
    "deployment": {
        "url": "http://localhost:3774",
        "expose": True,
    },
    "skills": [],
}

def handler(messages):
    return agent.run(input=messages)

bindufy(config, handler)
