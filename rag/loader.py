from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

UPLOAD_FOLDER = Path(__file__).parent.parent / "uploads"


# def load_resume(filename: str):

#     pdf_path = UPLOAD_FOLDER / filename

#     loader = PyPDFLoader(str(pdf_path))

#     documents = loader.load()

#     return documents

# def load_job_description(filename: str):

#     loader = PyPDFLoader(str(UPLOAD_FOLDER / filename))

#     return loader.load()

def load_resume():

    pdf_path = UPLOAD_FOLDER / "resume.pdf"

    loader = PyPDFLoader(str(pdf_path))

    return loader.load()


def load_job_description():

    pdf_path = UPLOAD_FOLDER / "job_description.pdf"

    loader = PyPDFLoader(str(pdf_path))

    return loader.load()