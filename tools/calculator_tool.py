"""
calculator_tool.py
"""

from langchain_core.tools import tool


@tool
def calculate_purchase_cost(
    quantity: int,
    unit_cost: float
) -> dict:
    """
    Calculate total procurement cost.
    """

    total = quantity * unit_cost

    return {

        "quantity": quantity,

        "unit_cost": unit_cost,

        "total_cost": total

    }