from services.fireworks_client import ask_llm

def competitor_agent(idea: str):

    prompt = f"""
You are a competitor intelligence analyst.

Startup Idea:
{idea}

Provide:

1. Top Competitors
2. Competition Level
3. Differentiation Opportunities
4. Moat Potential

Keep under 200 words.
"""

    return ask_llm(prompt)