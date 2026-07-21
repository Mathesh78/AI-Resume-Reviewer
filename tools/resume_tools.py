from rag.loader import load_resume
from rag.rag_pipelines import answer_question

# RESUME_NAME = "JeyaMathesh_Resume1.pdf"

from pathlib import Path

UPLOAD_FOLDER = Path("uploads")


def retrieve_resume(question: str) -> str:
    """
    Retrieve relevant resume information using RAG.
    """
    return answer_question(question)


def get_full_resume():

    pdf = UPLOAD_FOLDER / "resume.pdf"

    if not pdf.exists():

        raise FileNotFoundError(
            "Please upload your resume first."
        )

    documents = load_resume()

    resume = ""

    for doc in documents:

        resume += doc.page_content + "\n"

    return resume


def resume_statistics(text: str) -> dict:

    return {
        "Total Words": len(text.split()),
        "Characters": len(text),
        "Lines": len(text.splitlines())
    }


def validate_resume(text: str) -> list:

    checks = []

    sections = [
        "Skills",
        "Education",
        "Experience",
        "Projects",
        "Certifications"
    ]

    for section in sections:

        if section.lower() in text.lower():
            checks.append(f"✅ {section} Found")
        else:
            checks.append(f"❌ {section} Missing")

    if "@" in text:
        checks.append("✅ Email Found")
    else:
        checks.append("❌ Email Missing")

    return checks

from rag.loader import load_job_description


def get_full_job_description():

    pdf = UPLOAD_FOLDER / "job_description.pdf"

    if not pdf.exists():

        raise FileNotFoundError(
            "Please upload the Job Description first."
        )

    documents = load_job_description()

    job_description = ""

    for doc in documents:

        job_description += doc.page_content + "\n"

    return job_description