"""
supplier_service.py

Business Logic Layer for Procurement
"""

from tools.supplier_tool import (
    get_supplier_details,
    get_best_supplier
)

from tools.calculator_tool import (
    calculate_purchase_cost
)

from tools.risk_tool import (
    calculate_risk
)


class SupplierService:

    @staticmethod
    def fetch_supplier(supplier_id: str):

        return get_supplier_details.invoke(
            {
                "supplier_id": supplier_id
            }
        )

    @staticmethod
    def best_supplier():

        return get_best_supplier.invoke({})

    @staticmethod
    def calculate_cost(
        quantity: int,
        unit_cost: float
    ):

        return calculate_purchase_cost.invoke(
            {
                "quantity": quantity,
                "unit_cost": unit_cost
            }
        )

    @staticmethod
    def risk(
        current_stock: int,
        reorder_level: int,
        lead_time: int
    ):

        return calculate_risk.invoke(
            {
                "current_stock": current_stock,
                "reorder_level": reorder_level,
                "lead_time": lead_time
            }
        )

    @staticmethod
    def generate_purchase_order(
        inventory: dict,
        supplier: dict
    ):

        quantity = max(
            inventory["reorder_level"] * 2,
            50
        )

        cost = SupplierService.calculate_cost(
            quantity,
            inventory["unit_cost"]
        )

        return {

            "sku": inventory["sku"],

            "product_name": inventory["product_name"],

            "supplier": supplier["supplier_name"],

            "supplier_id": supplier["supplier_id"],

            "quantity": quantity,

            "unit_cost": inventory["unit_cost"],

            "lead_time_days":
                supplier["lead_time_days"],

            "total_cost":
                cost["total_cost"]

        }