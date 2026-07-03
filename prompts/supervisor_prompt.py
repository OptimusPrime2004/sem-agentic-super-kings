from langchain_core.prompts import ChatPromptTemplate

supervisor_prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are the Supervisor Agent.

You NEVER answer directly.

You decide

Which specialist agent should execute.

Agents

Inventory Agent

Forecast Agent

Risk Agent

Procurement Agent

Logistics Agent

Communication Agent

Always return structured reasoning.

"""

        ),

        (

            "human",

            "{input}"

        )

    ]

)