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

    return {

        "success": True,

        "supplier_id": row["supplier_id"],

        "supplier_name": row["supplier_name"],

        "reliability": row["reliability"],

        "lead_time_days": int(row["lead_time_days"]),

        "minimum_order_quantity":

            int(row["minimum_order_quantity"]),

        "rating": float(row["rating"])

    }


@tool
def get_best_supplier() -> dict:
    """
    Returns supplier with highest reliability and rating.
    """

    df = pd.read_csv(SUPPLIER_PATH)

    df = df.sort_values(
        by=["rating"],
        ascending=False
    )

    row = df.iloc[0]

    return {

        "supplier_id": row["supplier_id"],

        "supplier_name": row["supplier_name"],

        "rating": float(row["rating"]),

        "lead_time_days": int(row["lead_time_days"]),

        "reliability": row["reliability"]

    }