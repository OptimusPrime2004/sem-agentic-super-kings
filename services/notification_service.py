from tools.notification_tool import notify_customer


class NotificationService:

    @staticmethod
    def send(

        customer,

        order,

        message

    ):

        return notify_customer.invoke(

            {

                "customer_name": customer,

                "order_id": order,

                "message": message

            }

        )