"""Example of creating a research assistant agent using Bindu and Agno.

This example demonstrates how to create a simple research assistant agent
that uses DuckDuckGo for web searches and can be deployed as a Bindu agent.

Run with: bindu examples/agno_simple_example.py
Or set environment variables directly and run: python examples/agno_simple_example.py
"""

import os
from bindu.penguin.bindufy import bindufy
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openrouter import OpenRouter

from dotenv import load_dotenv

load_dotenv()

# Define your agent
agent = Agent(
    instructions=(
        "You are a witty joke-telling agent. "
        "Your job is to entertain users with clever, clean, and funny jokes. "
        "You can tell puns, dad jokes, tech jokes, and situational humor. "
        "Keep the tone light, playful, and human-like. "
        "If a topic is given, tailor the joke to that topic."
    ),
    model=OpenRouter(
        id="openai/gpt-oss-120b",
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[DuckDuckGoTools()],  # optional: for topical or trending jokes
)


# Configuration
# Note: Infrastructure configs (storage, scheduler, sentry, API keys) are now
# automatically loaded from environment variables. See .env.example for details.
config = {
    "author": "your.email@example.com",
    "name": "joke_agent",
    "description": "A research assistant agent",
    "deployment": {"url": "http://localhost:3773", "expose": True},
    "skills": ["skills/question-answering", "skills/pdf-processing"],
}


# Handler function
def handler(messages: list[dict[str, str]]):
    """Process messages and return agent response.

    Args:
        messages: List of message dictionaries containing conversation history

    Returns:
        Agent response result
    """
    result = agent.run(input=messages)
    return result


# Bindu-fy it
bindufy(config, handler)
