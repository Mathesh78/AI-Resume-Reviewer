from langgraph.graph import StateGraph, START, END

from graph.state import State

from graph.router import router_node, route

from graph.nodes import (

    summary_node,

    ats_node,

    interview_node,

    career_node,

    match_node


)

graph_builder = StateGraph(State)

graph_builder.add_node(

    "router",

    router_node

)

graph_builder.add_node(

    "summary",

    summary_node

)

graph_builder.add_node(

    "ats",

    ats_node

)

graph_builder.add_node(

    "interview",

    interview_node

)

graph_builder.add_node(

    "career",

    career_node

)

graph_builder.add_node(

    "match",

    match_node

)

graph_builder.add_edge(

    START,

    "router"

)


graph_builder.add_conditional_edges(

    "router",

    route,

    {

        "summary": "summary",

        "ats": "ats",

        "interview": "interview",

        "career": "career",

        "match": "match"


    }

)

graph_builder.add_edge(

    "summary",

    END

)

graph_builder.add_edge(

    "ats",

    END

)

graph_builder.add_edge(

    "interview",

    END

)

graph_builder.add_edge(

    "career",

    END

)

graph_builder.add_edge(

    "match",

    END

)



graph = graph_builder.compile()