from services.fireworks_client import ask_llm

def investor_agent(idea: str):

    prompt = f"""
You are a YC partner.

Startup Idea:
{idea}

Provide:

1. Invest / Maybe / Reject
2. Strengths
3. Weaknesses
4. Fundability Score (0-100)

Keep under 200 words.
"""

    return ask_llm(prompt)