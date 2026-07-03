"""
Forecasting Agent
"""

from tools.forecast_tool import ForecastTool


class ForecastingAgent:

    def __init__(self):

        self.tool = ForecastTool()

    def execute(self):

        forecasts = self.tool.forecast_all()

        high_demand = []

        for item in forecasts:

            if item["predicted_demand"] >= 50:

                high_demand.append(item)

        return {

            "forecast_count": len(forecasts),

            "high_demand_products": high_demand,

            "forecast_results": forecasts

        }