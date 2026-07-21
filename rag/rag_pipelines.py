from langchain_core.messages import HumanMessage, SystemMessage

from rag.retriever import fetch_context
from models.llm import llm


SYSTEM_PROMPT = """
You are an AI Resume Reviewer.

Use only the provided context.

Context:
{context}
"""


def answer_question(question):

    docs = fetch_context(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = SYSTEM_PROMPT.format(
        context=context
    )

    response = llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content=question)
    ])

    return response.content