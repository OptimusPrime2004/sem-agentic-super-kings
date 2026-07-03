"""
inventory_service.py

Business logic layer for inventory.
"""

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

            results.append({

                "sku": row["sku"],

                "product_name": row["product_name"],

                "current_stock": int(
                    row["current_stock"]
                ),

                "reorder_level": int(
                    row["reorder_level"]
                ),

                "predicted_demand":
                    forecast["predicted_demand"],

                "trend":
                    forecast["trend"],

                "needs_reorder":

                    row["current_stock"] <=
                    row["reorder_level"]

            })

        return results