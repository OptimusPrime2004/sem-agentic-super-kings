"""
Human In The Loop Node
"""


def approval_node(state):

    if state["approval_status"] == "Approved":

        state["logs"].append(
            "Manager Approved Purchase Order."
        )

    else:

        state["logs"].append(
            "Waiting For Manager Approval."
        )

    return state