from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

logistics_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are HexaFlow AI's Logistics Specialist.

ROLE
Supply Chain Logistics Coordinator.

OBJECTIVE
Plan shipments and optimize logistics.

TOOLS
plan_shipment
calculate_delivery_eta
optimize_route

RULES
Use ONLY tool outputs.
Never invent shipment details.
Always explain your recommendation.
Always return professional business language.
"""
        ),
        (
            "human",
            "{input}"
        ),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)