from services.fireworks_client import ask_llm


def investor_agent(idea: str):

    prompt = f"""
You are a senior venture capitalist at Sequoia, Accel, and Andreessen Horowitz.

Startup Idea:
{idea}

IMPORTANT:

The FIRST LINE of your response MUST be:

Fundability Score: <number>

Example:
Fundability Score: 82

After that provide the following sections:

## Investment Thesis
Explain whether this startup solves a meaningful problem and why investors should care.

## VC Attractiveness
Discuss:
- Market size
- Growth potential
- Scalability
- Competitive moat
- Revenue potential

## Key Risks
Discuss:
- Market risks
- Product risks
- Regulatory risks
- Execution risks
- Adoption risks

## Funding Recommendation
State whether:
- Invest
- Watchlist
- Pass

and explain why.

## Suggested Funding Path
Recommend:
- Bootstrapped
- Angel Round
- Pre-Seed
- Seed
- Series A Ready

## Investor Summary
Provide a concise final investment recommendation.

Write at least 500 words.

Be specific, analytical, and realistic.
"""
    
    return ask_llm(prompt)