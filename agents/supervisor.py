from langchain_openai import AzureChatOpenAI

from prompts.supervisor_prompt import supervisor_prompt

from config.settings import *

llm = AzureChatOpenAI(

    azure_endpoint=AZURE_ENDPOINT,

    api_key=AZURE_API_KEY,

    azure_deployment=AZURE_DEPLOYMENT,

    api_version=AZURE_API_VERSION,

    temperature=0

)


def supervisor(state):

    question = state["user_query"]

    response = llm.invoke(

        supervisor_prompt.format_messages(

            input=question

        )

    )

    state["final_response"] = response.content

    state["logs"].append(

        "Supervisor executed."

    )

    return state