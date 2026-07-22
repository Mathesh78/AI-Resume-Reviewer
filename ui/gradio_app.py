import shutil
from pathlib import Path

import gradio as gr
from langchain_core.messages import HumanMessage

from graph.builder import graph
from reports.pdf_report import create_ats_pdf


# ======================================================
# Upload Folder
# ======================================================

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


# ======================================================
# Upload Resume
# ======================================================

def upload_resume(file):

    if file is None:
        return "Please upload a resume."

    shutil.copy(file, UPLOAD_FOLDER / "resume.pdf")

    return "Resume uploaded successfully."


# ======================================================
# Upload Job Description
# ======================================================

def upload_jd(file):

    if file is None:
        return "Please upload a Job Description."

    shutil.copy(file, UPLOAD_FOLDER / "job_description.pdf")

    return "Job Description uploaded successfully."


# ======================================================
# Ask AI
# ======================================================

def ask_ai(question):

    if question.strip() == "":
        return "Please enter a question.", None

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=question)
            ],
            "route": "",
            "answer": "",
            "job_description": ""
        }
    )

    answer = result["answer"]

    pdf = create_ats_pdf(question, answer)

    return answer, pdf


# ======================================================
# UI
# ======================================================

with gr.Blocks(title="AI Resume Reviewer") as demo:

    gr.Markdown("# AI Resume Reviewer")

    gr.Markdown("## Upload Resume")

    resume = gr.File(
        file_types=[".pdf"]
    )

    resume_btn = gr.Button("Upload Resume")

    resume_status = gr.Textbox(
        label="Status"
    )

    resume_btn.click(
        upload_resume,
        inputs=resume,
        outputs=resume_status
    )

    gr.Markdown("---")

    gr.Markdown("## Upload Job Description")

    jd = gr.File(
        file_types=[".pdf"]
    )

    jd_btn = gr.Button("Upload Job Description")

    jd_status = gr.Textbox(
        label="Status"
    )

    jd_btn.click(
        upload_jd,
        inputs=jd,
        outputs=jd_status
    )

    gr.Markdown("---")

    question = gr.Textbox(
        label="Ask Anything",
        placeholder="Example: Generate ATS Score"
    )

    ask_btn = gr.Button("Ask")

    answer = gr.Textbox(
        label="Response",
        lines=25
    )

    report = gr.File(
        label="Download Report"
    )

    ask_btn.click(
        ask_ai,
        inputs=question,
        outputs=[
            answer,
            report
        ]
    )


if __name__ == "__main__":
    demo.launch()