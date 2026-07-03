from pathlib import Path
import pandas as pd


class InventoryTool:

    def __init__(self):

        self.inventory = pd.read_csv(
            Path("data") / "inventory.csv"
        )

    def get_all_inventory(self):

        return self.inventory

    def get_inventory_by_sku(self, sku: str):

        result = self.inventory[
            self.inventory["sku"] == sku
        ]

        if result.empty:

            return None

        return result.iloc[0].to_dict()

    def get_low_stock_items(self):

        low_stock = self.inventory[
            self.inventory["current_stock"]
            <=
            self.inventory["reorder_level"]
        ]

        return low_stock.to_dict("records")