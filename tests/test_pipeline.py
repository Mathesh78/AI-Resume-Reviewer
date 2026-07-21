from rag.rag_pipelines import answer_question

response = answer_question(
    "Summarize the candidate's resume."
)

print("=" * 80)

print(response)

print("=" * 80)