from langchain_core.tools import tool


@tool
def get_shipping_plan(destination: str, weight: float):

    """
    Mock Shipping API
    """

    carriers = [

        {
            "carrier": "BlueDart",
            "eta": "2 Days",
            "cost": 120
        },

        {
            "carrier": "Delhivery",
            "eta": "3 Days",
            "cost": 95
        },

        {
            "carrier": "DTDC",
            "eta": "4 Days",
            "cost": 80
        }

    ]

    best = min(
        carriers,
        key=lambda x: x["cost"]
    )

    return {

        "destination": destination,

        "weight": weight,

        "recommended_carrier": best

    }