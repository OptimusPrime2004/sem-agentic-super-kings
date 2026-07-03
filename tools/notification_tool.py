from langchain_core.tools import tool


@tool
def notify_customer(

    customer_name: str,

    order_id: str,

    message: str

):

    """
    Mock Notification Tool
    """

    return {

        "status": "SUCCESS",

        "customer": customer_name,

        "order_id": order_id,

        "message": message

    }