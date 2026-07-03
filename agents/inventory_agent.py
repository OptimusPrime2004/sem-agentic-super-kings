"""
Inventory Agent
"""

from services.inventory_service import InventoryService


class InventoryAgent:

    def __init__(self):

        self.service = InventoryService()

    def execute(self):

        analysis = self.service.analyze_inventory()

        low_stock = []

        for item in analysis:

            if item["needs_reorder"]:

                low_stock.append(item)

        return {

            "total_items": len(analysis),

            "low_stock_count": len(low_stock),

            "low_stock_items": low_stock
        }