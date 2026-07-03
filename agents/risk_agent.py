"""
risk_agent.py

HexaFlow AI
Risk Assessment Agent
"""

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import AzureChatOpenAI

from config.settings import (
    AZURE_ENDPOINT,
    AZURE_API_KEY,
    AZURE_API_VERSION,
    AZURE_DEPLOYMENT
)

from prompts.risk_prompt import risk_prompt

from tools.risk_tool import calculate_risk

from services.supplier_service import SupplierService


llm = AzureChatOpenAI(

    azure_endpoint=AZURE_ENDPOINT,

    api_key=AZURE_API_KEY,

    api_version=AZURE_API_VERSION,

    azure_deployment=AZURE_DEPLOYMENT,

    temperature=0

)

tools = [

    calculate_risk

]

agent = create_tool_calling_agent(

    llm=llm,

    prompt=risk_prompt,

    tools=tools

)

risk_agent = AgentExecutor(

    agent=agent,

    tools=tools,

    verbose=True

)


def assess_procurement_risk(inventory_item: dict):

    """
    Returns structured procurement risk.
    """

    supplier = SupplierService.fetch_supplier(

        inventory_item["supplier_id"]

    )

    risk = SupplierService.risk(

        current_stock=inventory_item["current_stock"],

        reorder_level=inventory_item["reorder_level"],

        lead_time=supplier["lead_time_days"]

    )

    return {

        "sku": inventory_item["sku"],

        "product_name": inventory_item["product_name"],

        "supplier": supplier["supplier_name"],

        "risk_score": risk["risk_score"],

        "risk_level": risk["risk_level"],

        "recommendation":

        "Immediate Procurement"

        if risk["risk_level"] == "HIGH"

        else "Monitor Inventory"

    }


def run_risk_agent(question: str):

    return risk_agent.invoke(

        {

            "input": question

        }

    )