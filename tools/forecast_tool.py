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
            Path("data") / "sales_history.csv",
            parse_dates=["date"]
        )

        self.sales.sort_values(["sku", "date"], inplace=True)

        self.sales["last_7_days"] = self.sales.groupby("sku")["units_sold"].transform(
            lambda s: s.rolling(7, min_periods=1).sum().shift(1).fillna(0)
        )
        self.sales["last_14_days"] = self.sales.groupby("sku")["units_sold"].transform(
            lambda s: s.rolling(14, min_periods=1).sum().shift(1).fillna(0)
        )
        self.sales["last_30_days"] = self.sales.groupby("sku")["units_sold"].transform(
            lambda s: s.rolling(30, min_periods=1).sum().shift(1).fillna(0)
        )

        if "trend" not in self.sales.columns:
            self.sales["trend"] = self.sales.groupby("sku")["units_sold"].transform(
                lambda s: s.diff().fillna(0)
            )
            self.sales["trend"] = self.sales["trend"].apply(self._trend_label)

    def _trend_label(self, diff_value):
        if diff_value > 0:
            return "up"
        if diff_value < 0:
            return "down"
        return "stable"

    def forecast(self, sku: str):

        row = self.sales[self.sales["sku"] == sku]

        if row.empty:
            return None

        row = row.iloc[-1]

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

        latest_sales = self.sales.groupby("sku").tail(1)

        for _, row in latest_sales.iterrows():

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