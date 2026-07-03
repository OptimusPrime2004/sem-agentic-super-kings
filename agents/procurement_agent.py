"""
procurement_agent.py

HexaFlow AI
Procurement Agent
"""

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import AzureChatOpenAI

from config.settings import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_KEY,
    AZURE_API_VERSION,
    AZURE_DEPLOYMENT
)

from prompts.procurement_prompt import procurement_prompt

from tools.supplier_tool import (
    get_supplier_details,
    get_best_supplier
)

from tools.calculator_tool import (
    calculate_purchase_cost
)

from services.supplier_service import SupplierService


llm = AzureChatOpenAI(

    azure_endpoint=AZURE_OPENAI_ENDPOINT,

    api_key=AZURE_OPENAI_KEY,

    api_version=AZURE_API_VERSION,

    azure_deployment=AZURE_DEPLOYMENT,

    temperature=0

)

tools = [

    get_supplier_details,

    get_best_supplier,

    calculate_purchase_cost

]

agent = create_tool_calling_agent(

    llm=llm,

    prompt=procurement_prompt,

    tools=tools

)

procurement_agent = AgentExecutor(

    agent=agent,

    tools=tools,

    verbose=True

)


def create_purchase_order(inventory_item: dict):

    """
    Creates Purchase Order using supplier service.
    """

    supplier = SupplierService.fetch_supplier(

        inventory_item["supplier_id"]

    )

    purchase_order = SupplierService.generate_purchase_order(

        inventory_item,

        supplier

    )

    return purchase_order


def run_procurement_agent(question: str):

    """
    Natural Language Procurement Query
    """

    return procurement_agent.invoke(

        {

            "input": question

        }

    )