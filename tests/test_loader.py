from rag.loader import load_resume

documents = load_resume("JeyaMathesh_Resume1.pdf")

print(documents[0].page_content)