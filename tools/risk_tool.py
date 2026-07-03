"""
risk_tool.py

Business Risk Assessment Tool
"""

from langchain_core.tools import tool


@tool
def calculate_risk(
    current_stock: int,
    reorder_level: int,
    lead_time: int
) -> dict:
    """
    Calculates procurement risk.
    """

    score = 0

    if current_stock <= reorder_level:
        score += 40

    if lead_time >= 8:
        score += 30

    gap = reorder_level - current_stock

    if gap >= 15:
        score += 30

    if score >= 70:
        level = "HIGH"

    elif score >= 40:
        level = "MEDIUM"

    else:
        level = "LOW"

    return {

        "risk_score": score,

        "risk_level": level

    }