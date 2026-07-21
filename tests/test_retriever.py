from rag.retriever import fetch_context

docs = fetch_context(
    "What technical skills does the candidate have?"
)

print("=" * 80)
print(f"Retrieved {len(docs)} Documents")
print("=" * 80)

for i, doc in enumerate(docs):

    print(f"\nChunk {i+1}\n")

    print(doc.page_content)

    print("-" * 80)