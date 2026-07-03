from typing import TypedDict, List, Dict


class WorkflowState(TypedDict):

    user_query: str

    inventory: Dict

    forecast: Dict

    procurement: Dict

    risk: Dict

    logistics: Dict

    communication: Dict

    approval_status: str

    logs: List[str]

    final_response: str