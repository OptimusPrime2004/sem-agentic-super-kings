"""
communication_agent.py
"""

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import AzureChatOpenAI

from config.settings import (
    AZURE_ENDPOINT,
    AZURE_API_KEY,
    AZURE_API_VERSION,
    AZURE_DEPLOYMENT
)

from prompts.communication_prompt import communication_prompt

from tools.notification_tool import notify_customer

llm = AzureChatOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION,
    azure_deployment=AZURE_DEPLOYMENT,
    temperature=0.3
)

tools = [
    notify_customer
]

agent = create_tool_calling_agent(
    llm=llm,
    prompt=communication_prompt,
    tools=tools
)

communication_agent = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


def run_communication_agent(question: str):

    return communication_agent.invoke(
        {
            "input": question
        }
    )