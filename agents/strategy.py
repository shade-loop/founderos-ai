from services.fireworks_client import ask_llm

def strategy_agent(idea: str):

    prompt = f"""
You are a startup strategist.

Startup Idea:
{idea}

Provide:

1. MVP Features
2. 30 Day Roadmap
3. Go To Market Plan
4. Revenue Model

Keep under 200 words.
"""

    return ask_llm(prompt)