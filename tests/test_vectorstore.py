from rag.loader import load_resume
from rag.splitter import create_chunks
from rag.vectorstore import create_vectorstore

documents = load_resume("JeyaMathesh_Resume1.pdf")

chunks = create_chunks(documents)

vectorstore = create_vectorstore(chunks)

print("=" * 80)
print("Vector Database Created Successfully")
print("=" * 80)

collection = vectorstore._collection

print(f"Vectors Stored : {collection.count()}")