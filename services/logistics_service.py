from tools.shipping_tool import get_shipping_plan


class LogisticsService:

    @staticmethod
    def create_plan(

        destination,

        weight

    ):

        return get_shipping_plan.invoke(

            {

                "destination": destination,

                "weight": weight

            }

        )