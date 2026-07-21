from pathlib import Path

from langchain_chroma import Chroma

from rag.embeddings import embeddings

DB_PATH = Path(__file__).parent.parent / "vector_db"


def create_vectorstore(chunks):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(DB_PATH)
    )

    return vectorstore