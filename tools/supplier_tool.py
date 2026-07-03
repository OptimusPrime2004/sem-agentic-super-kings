"""
supplier_tool.py

LangChain Tool for Supplier Lookup
"""

from pathlib import Path
import pandas as pd

from langchain_core.tools import tool

SUPPLIER_PATH = Path("data/suppliers.csv")


@tool
def get_supplier_details(supplier_id: str) -> dict:
    """
    Fetch supplier information using supplier_id.
    """

    df = pd.read_csv(SUPPLIER_PATH)

    supplier = df[
        df["supplier_id"].str.upper() == supplier_id.upper()
    ]

    if supplier.empty:

        return {
            "success": False,
            "message": f"Supplier {supplier_id} not found."
        }

    row = supplier.iloc[0]

    rating = float(row["reliability_score"])
    if "on_time_rate" in row:
        rating = (rating + float(row["on_time_rate"])) / 2

    lead_time_status = str(row.get("lead_time_status", ""))
    lead_time_days = 0
    if "day" in lead_time_status.lower():
        digits = [int(token) for token in lead_time_status.split() if token.isdigit()]
        if digits:
            lead_time_days = digits[0]
    elif "on-time" in lead_time_status.lower() or "on time" in lead_time_status.lower():
        lead_time_days = 2
    else:
        lead_time_days = 7

    minimum_order_quantity = int(row.get("minimum_order_quantity", 1))

    return {

        "success": True,

        "supplier_id": row["supplier_id"],

        "supplier_name": row["supplier_name"],

        "reliability": float(row["reliability_score"]),

        "lead_time_days": lead_time_days,

        "minimum_order_quantity":

            minimum_order_quantity,

        "rating": rating

    }


@tool
def get_best_supplier() -> dict:
    """
    Returns supplier with highest reliability and rating.
    """

    df = pd.read_csv(SUPPLIER_PATH)
    df["rating"] = df["reliability_score"].astype(float)
    if "on_time_rate" in df.columns:
        df["rating"] = (
            df["rating"] + df["on_time_rate"].astype(float)
        ) / 2

    df = df.sort_values(
        by=["rating"],
        ascending=False
    )

    row = df.iloc[0]

    lead_time_status = str(row.get("lead_time_status", ""))
    lead_time_days = 0
    if "day" in lead_time_status.lower():
        digits = [int(token) for token in lead_time_status.split() if token.isdigit()]
        if digits:
            lead_time_days = digits[0]
    elif "on-time" in lead_time_status.lower() or "on time" in lead_time_status.lower():
        lead_time_days = 2
    else:
        lead_time_days = 7

    return {

        "supplier_id": row["supplier_id"],

        "supplier_name": row["supplier_name"],

        "rating": float(row["rating"]),

        "lead_time_days": lead_time_days,

        "reliability": row["reliability_score"]

    }