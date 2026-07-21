from graph.state import State


def router_node(state: State):

    question = state["messages"][-1].content.lower()

    if "summary" in question:

        route = "summary"

    elif "ats" in question:

        route = "ats"

    elif "interview" in question:

        route = "interview"

    elif "career" in question:

        route = "career"

    elif "match" in question or "job description" in question:

        route = "match"

    else:

        route = "summary"

    return {

        "route": route

    }


def route(state: State):

    return state["route"]