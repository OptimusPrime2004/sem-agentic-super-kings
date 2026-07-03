"""
inventory_service.py

Business logic layer for inventory.
"""

import pandas as pd

from tools.inventory_tool import InventoryTool
from tools.forecast_tool import ForecastTool


class InventoryService:

    def __init__(self):

        self.inventory_tool = InventoryTool()
        self.forecast_tool = ForecastTool()

    def analyze_inventory(self):

        inventory = self.inventory_tool.get_all_inventory()

        results = []

        for _, row in inventory.iterrows():

            forecast = self.forecast_tool.forecast(
                row["sku"]
            )

            product_name = row.get("product_name", None)
            if product_name is None or pd.isna(product_name):
                product_name = row["sku"]

            current_stock = int(row["current_stock"])
            reorder_level = int(row["reorder_level"])

            results.append({

                "sku": row["sku"],

                "product_name": product_name,

                "current_stock": current_stock,

                "reorder_level": reorder_level,

                "predicted_demand":
                    forecast["predicted_demand"],

                "trend":
                    forecast["trend"],

                "needs_reorder":

                    current_stock <=
                    reorder_level

            })

        return results