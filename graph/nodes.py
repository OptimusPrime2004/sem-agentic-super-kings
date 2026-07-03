"""
graph/nodes.py

LangGraph Nodes
"""

from agents.inventory_agent import run_inventory_agent
from agents.forecasting_agent import run_forecasting_agent
from agents.procurement_agent import run_procurement_agent
from agents.risk_agent import run_risk_agent
from agents.logistics_agent import run_logistics_agent
from agents.communication_agent import run_communication_agent


def inventory_node(state):

    result = run_inventory_agent(state["user_query"])

    state["inventory"] = result

    state["logs"].append("Inventory Agent Executed")

    return state


def forecast_node(state):

    result = run_forecasting_agent(state["user_query"])

    state["forecast"] = result

    state["logs"].append("Forecast Agent Executed")

    return state


def procurement_node(state):

    result = run_procurement_agent(state["user_query"])

    state["procurement"] = result

    state["logs"].append("Procurement Agent Executed")

    return state


def risk_node(state):

    result = run_risk_agent(state["user_query"])

    state["risk"] = result

    state["logs"].append("Risk Agent Executed")

    return state


def logistics_node(state):

    result = run_logistics_agent(state["user_query"])

    state["logistics"] = result

    state["logs"].append("Logistics Agent Executed")

    return state


def communication_node(state):

    result = run_communication_agent(state["user_query"])

    state["communication"] = result

    state["logs"].append("Communication Agent Executed")

    return state