import shutil
from pathlib import Path
import requests


import gradio as gr
from langchain_core.messages import HumanMessage

from graph.builder import graph
from reports.pdf_report import create_ats_pdf


import requests

def upload_resume(file):

    with open(file, "rb") as f:

        response = requests.post(
            "http://127.0.0.1:8000/upload-resume",
            files={
                "file": (
                    "resume.pdf",      # filename
                    f,                 # file object
                    "application/pdf" # MIME type
                )
            }
        )

    print(response.status_code)
    print(response.text)

    return response.json()["message"]

# ======================================================
# Upload Job Description
# ======================================================


def upload_jd(file):

    with open(file, "rb") as f:

        response = requests.post(
            "http://127.0.0.1:8000/upload-job-description",
            files={
                "file": (
                    "job_description.pdf",
                    f,
                    "application/pdf"
                )
            }
        )

    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        return response.json()["message"]

    return response.text
# ======================================================
# Ask AI
# ======================================================

# def ask_ai(question):

#     response = requests.post(

#         "http://127.0.0.1:8000/chat",

#         json={
#             "question": question
#         }

#     )

#     answer = response.json()["response"]

#     pdf = create_ats_pdf(question, answer)

#     return answer, pdf


def ask_ai(question):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={
            "question": question
        }
    )

    print("Status Code:", response.status_code)
    print("Response Text:")
    print(response.text)

    if response.status_code != 200:
        return f"Server Error:\n{response.text}", None

    answer = response.json()["response"]

    pdf = create_ats_pdf(question, answer)

    return answer, pdf

# ======================================================
# Gradio UI
# ======================================================

with gr.Blocks(title="AI Resume Reviewer") as demo:

    gr.Markdown("# AI Resume Reviewer")

    # ---------------- Resume Upload ----------------

    gr.Markdown("## Upload Resume")

    resume = gr.File(file_types=[".pdf"])
    resume_btn = gr.Button("Upload Resume")
    resume_status = gr.Textbox(label="Status")

    resume_btn.click(
        fn=upload_resume,
        inputs=resume,
        outputs=resume_status
    )

    gr.Markdown("---")

    # ---------------- JD Upload ----------------

    gr.Markdown("## Upload Job Description")

    jd = gr.File(file_types=[".pdf"])
    jd_btn = gr.Button("Upload Job Description")
    jd_status = gr.Textbox(label="Status")

    jd_btn.click(
        fn=upload_jd,
        inputs=jd,
        outputs=jd_status
    )

    gr.Markdown("---")

    # ---------------- Chat ----------------

    question = gr.Textbox(
        label="Ask Anything",
        placeholder="Example: Generate ATS Score"
    )

    ask = gr.Button("Ask")

    output = gr.Textbox(
        label="Response",
        lines=25
    )

    download = gr.File(
        label="Download Report"
    )

    # IMPORTANT:
    # This must be INSIDE the Blocks context

    ask.click(
        fn=ask_ai,
        inputs=question,
        outputs=[
            output,
            download
        ]
    )

# ======================================================
# Launch App
# ======================================================

demo.launch(share=True)