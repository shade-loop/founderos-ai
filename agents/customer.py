from services.fireworks_client import ask_llm

def customer_agent(idea: str):

    prompt = f"""
You are a customer research specialist.

Startup Idea:
{idea}

Provide:

1. Ideal Customer Profile
2. Pain Points
3. Adoption Barriers
4. Customer Demand

Keep under 200 words.
"""

    return ask_llm(prompt)