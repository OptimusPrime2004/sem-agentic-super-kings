"""
logistics_agent.py

HexaFlow AI
"""

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import AzureChatOpenAI

from config.settings import (
    AZURE_ENDPOINT,
    AZURE_API_KEY,
    AZURE_API_VERSION,
    AZURE_DEPLOYMENT
)

from prompts.logistics_prompt import logistics_prompt

from tools.shipping_tool import get_shipping_plan

llm = AzureChatOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION,
    azure_deployment=AZURE_DEPLOYMENT,
    temperature=0
)

tools = [
    get_shipping_plan
]

agent = create_tool_calling_agent(
    llm=llm,
    prompt=logistics_prompt,
    tools=tools
)

logistics_agent = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


def run_logistics_agent(question: str):

    return logistics_agent.invoke(
        {
            "input": question
        }
    )