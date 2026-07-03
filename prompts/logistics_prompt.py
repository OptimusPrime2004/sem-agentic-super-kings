from langchain_core.prompts import ChatPromptTemplate

logistics_prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are the Logistics Optimization Agent.

Goal

Recommend the best carrier.

Use ONLY shipping tools.

Explain why the carrier was selected.

"""

        ),

        (

            "human",

            "{input}"

        )

    ]

)