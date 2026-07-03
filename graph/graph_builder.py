from langgraph.graph import StateGraph, END

from graph.state import WorkflowState

from graph.nodes import (

    inventory_node,

    forecast_node,

    procurement_node,

    risk_node,

    logistics_node,

    communication_node

)

from graph.approval_node import approval_node

from graph.edges import approval_router


workflow = StateGraph(WorkflowState)

workflow.add_node(
    "inventory",
    inventory_node
)

workflow.add_node(
    "forecast",
    forecast_node
)

workflow.add_node(
    "risk",
    risk_node
)

workflow.add_node(
    "procurement",
    procurement_node
)

workflow.add_node(
    "approval",
    approval_node
)

workflow.add_node(
    "logistics",
    logistics_node
)

workflow.add_node(
    "communication",
    communication_node
)

workflow.set_entry_point(
    "inventory"
)

workflow.add_edge(
    "inventory",
    "forecast"
)

workflow.add_edge(
    "forecast",
    "risk"
)

workflow.add_edge(
    "risk",
    "procurement"
)

workflow.add_edge(
    "procurement",
    "approval"
)

workflow.add_conditional_edges(

    "approval",

    approval_router,

    {

        "approval": "approval",

        "logistics": "logistics"

    }

)

workflow.add_edge(
    "logistics",
    "communication"
)

workflow.add_edge(
    "communication",
    END
)

graph = workflow.compile()