from rag.loader import load_resume
from rag.splitter import create_chunks

documents = load_resume("JeyaMathesh_Resume1.pdf")

chunks = create_chunks(documents)

print(f"Total Chunks : {len(chunks)}")

for i, chunk in enumerate(chunks):

    print("=" * 80)
    print(f"Chunk {i+1}")
    print("=" * 80)

    print(chunk.page_content)