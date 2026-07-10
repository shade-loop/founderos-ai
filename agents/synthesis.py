from services.fireworks_client import ask_llm

def synthesis_agent(market, competitor, customer, investor, strategy):

    prompt = f"""
You are a venture capital investment committee.

Analyze:

MARKET:
{market}

COMPETITOR:
{competitor}

CUSTOMER:
{customer}

INVESTOR:
{investor}

STRATEGY:
{strategy}

Return EXACTLY:

Venture Score: <0-100>
Verdict: <BUILD/MAYBE/REJECT>
Confidence: <0-100>
Risk Level: <LOW/MEDIUM/HIGH>

Summary:
<3 sentence executive summary>
"""

    return ask_llm(prompt)