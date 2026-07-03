"""
analytics_tool.py
"""


from langchain_core.tools import tool


@tool
def generate_dashboard_metrics(

    inventory_count: int,

    low_stock: int,

    purchase_orders: int,

    delayed_orders: int

):

    return {

        "inventory": inventory_count,

        "low_stock": low_stock,

        "purchase_orders": purchase_orders,

        "delayed_orders": delayed_orders

    }