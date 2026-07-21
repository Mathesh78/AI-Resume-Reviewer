
from langchain_core.messages import HumanMessage

from app.schemas import QuestionRequest

from graph.builder import graph

import shutil


from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from pathlib import Path


router = APIRouter()


UPLOAD_FOLDER = Path("uploads")

UPLOAD_FOLDER.mkdir(exist_ok=True)


@router.post("/chat")
def chat(request: QuestionRequest):

    try:
        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=request.question)
                ],
                "route": "",
                "answer": "",
                "job_description": ""
            }
        )

        return {
            "response": result["answer"]
        }

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
 
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    try:

        file_path = UPLOAD_FOLDER / "resume.pdf"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {
            "message": "Resume uploaded successfully."
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.post("/upload-job-description")
async def upload_job_description(file: UploadFile = File(...)):

    file_path = UPLOAD_FOLDER / "job_description.pdf"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {

        "message": "Job Description uploaded successfully",

        "filename": file.filename

    }