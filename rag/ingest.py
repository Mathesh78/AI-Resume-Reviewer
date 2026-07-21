from rag.loader import load_resume
from rag.splitter import create_chunks
from rag.vectorstore import create_vectorstore

documents = load_resume("JeyaMathesh_Resume1.pdf")

chunks = create_chunks(documents)

create_vectorstore(chunks)

print("Vector DB Created Successfully")