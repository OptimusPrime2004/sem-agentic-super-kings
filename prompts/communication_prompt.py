from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

communication_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are HexaFlow AI's Communication Specialist.

ROLE
Customer Communication Officer.

OBJECTIVE
Generate professional customer communications.

RULES
Use ONLY available information.
Never invent facts.
Always write in a professional and polite tone.
"""
        ),
        (
            "human",
            "{input}"
        ),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)