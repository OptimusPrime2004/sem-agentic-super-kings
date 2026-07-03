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

workflow.add_node("inventory_agent", inventory_node)
workflow.add_node("forecast_agent", forecast_node)
workflow.add_node("risk_agent", risk_node)
workflow.add_node("procurement_agent", procurement_node)
workflow.add_node("approval", approval_node)
workflow.add_node("logistics_agent", logistics_node)
workflow.add_node("communication_agent", communication_node)

workflow.set_entry_point("inventory_agent")

workflow.add_edge("inventory_agent", "forecast_agent")
workflow.add_edge("forecast_agent", "risk_agent")
workflow.add_edge("risk_agent", "procurement_agent")
workflow.add_edge("procurement_agent", "approval")

workflow.add_conditional_edges(
    "approval",
    approval_router,
    {
        "approval": END,
        "logistics": "logistics_agent"
    }
)

workflow.add_edge("logistics_agent", "communication_agent")
workflow.add_edge("communication_agent", END)

graph = workflow.compile()