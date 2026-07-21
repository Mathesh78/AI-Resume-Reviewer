from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph.message import add_messages


class State(TypedDict):

    messages: Annotated[list, add_messages]

    route: str

    answer: str

    job_description: str