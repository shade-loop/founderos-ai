from services.fireworks_client import ask_llm

def market_agent(idea: str):

    prompt = f"""
You are a venture market analyst.

Startup Idea:
{idea}

Provide:

1. Market Opportunity Score (0-100)
2. Market Size
3. Growth Potential
4. Key Risks

Keep under 200 words.
"""

    return ask_llm(prompt)