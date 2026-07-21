from pathlib import Path

from langchain_chroma import Chroma

from rag.embeddings import embeddings

DB_PATH = Path(__file__).parent.parent / "vector_db"

vectorstore = Chroma(
    persist_directory=str(DB_PATH),
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)


def fetch_context(question):

    return retriever.invoke(question)