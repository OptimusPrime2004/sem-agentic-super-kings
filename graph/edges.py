"""
Conditional Routing
"""


def approval_router(state):

    if state["approval_status"] == "Approved":

        return "logistics"

    return "approval"