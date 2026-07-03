"""
forecast_tool.py

Simple demand forecasting tool.
Uses historical sales to estimate short-term demand.
"""

from pathlib import Path
import pandas as pd


class ForecastTool:

    def __init__(self):

        self.sales = pd.read_csv(
            Path("data") / "sales_history.csv"
        )

    def forecast(self, sku: str):

        row = self.sales[
            self.sales["sku"] == sku
        ]

        if row.empty:
            return None

        row = row.iloc[0]

        prediction = int(
            (
                row["last_7_days"] * 0.5 +
                row["last_14_days"] * 0.3 +
                row["last_30_days"] * 0.2
            )
        )

        return {
            "sku": sku,
            "predicted_demand": prediction,
            "trend": row["trend"]
        }

    def forecast_all(self):

        forecasts = []

        for _, row in self.sales.iterrows():

            prediction = int(
                (
                    row["last_7_days"] * 0.5 +
                    row["last_14_days"] * 0.3 +
                    row["last_30_days"] * 0.2
                )
            )

            forecasts.append({
                "sku": row["sku"],
                "predicted_demand": prediction,
                "trend": row["trend"]
            })

        return forecasts