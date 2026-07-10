import asyncio
import re

from agents.market import market_agent
from agents.competitor import competitor_agent
from agents.customer import customer_agent
from agents.investor import investor_agent
from agents.strategy import strategy_agent
from agents.synthesis import synthesis_agent


async def run_analysis(idea: str):

    loop = asyncio.get_running_loop()

    market_task = loop.run_in_executor(
        None,
        market_agent,
        idea
    )

    competitor_task = loop.run_in_executor(
        None,
        competitor_agent,
        idea
    )

    customer_task = loop.run_in_executor(
        None,
        customer_agent,
        idea
    )

    investor_task = loop.run_in_executor(
        None,
        investor_agent,
        idea
    )

    strategy_task = loop.run_in_executor(
        None,
        strategy_agent,
        idea
    )

    market, competitor, customer, investor, strategy = await asyncio.gather(
        market_task,
        competitor_task,
        customer_task,
        investor_task,
        strategy_task
    )

    synthesis = synthesis_agent(
        market,
        competitor,
        customer,
        investor,
        strategy
    )

    # ---------- Extract scores ----------

    venture_score = re.search(
        r"Venture Score:\s*(\d+)",
        synthesis,
        re.IGNORECASE
    )

    verdict = re.search(
        r"Verdict:\s*([A-Z]+)",
        synthesis,
        re.IGNORECASE
    )

    confidence = re.search(
        r"Confidence:\s*(\d+)",
        synthesis,
        re.IGNORECASE
    )

    market_score = re.search(
        r"Market Opportunity Score.*?(\d+)",
        market,
        re.IGNORECASE | re.DOTALL
    )

    fundability_score = re.search(
        r"Fundability Score[:\s]*(\d+)",
        investor,
        re.IGNORECASE | re.DOTALL
    )

    return {
        # Dashboard metrics
        "venture_score": (
            int(venture_score.group(1))
            if venture_score else 0
        ),

        "market_score": (
            int(market_score.group(1))
            if market_score else 0
        ),

        "fundability_score": (
            int(fundability_score.group(1))
            if fundability_score else 0
        ),

        "confidence": (
            int(confidence.group(1))
            if confidence else 0
        ),

        "verdict": (
            verdict.group(1)
            if verdict else "UNKNOWN"
        ),

        # Full reports
        "synthesis": synthesis,
        "market": market,
        "competitor": competitor,
        "customer": customer,
        "investor": investor,
        "strategy": strategy
    }