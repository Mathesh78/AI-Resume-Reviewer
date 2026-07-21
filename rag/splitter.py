from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)