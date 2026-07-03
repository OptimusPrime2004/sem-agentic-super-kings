from langchain_core.prompts import ChatPromptTemplate

communication_prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are the Customer Communication Agent.

Generate professional customer notifications.

Keep the tone

empathetic

professional

clear

short.

"""

        ),

        (

            "human",

            "{input}"

        )

    ]

)