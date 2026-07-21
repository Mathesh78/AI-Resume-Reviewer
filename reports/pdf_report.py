from pathlib import Path
import re

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

OUTPUT_FOLDER = Path("generated_reports")
OUTPUT_FOLDER.mkdir(exist_ok=True)


def create_ats_pdf(title: str, content: str):

    # Remove invalid filename characters
    safe_title = re.sub(r'[\\/:*?"<>|]', "", title)

    # Optional: replace spaces with underscores
    safe_title = safe_title.replace(" ", "_")

    pdf_path = OUTPUT_FOLDER / f"{safe_title}.pdf"

    styles = getSampleStyleSheet()

    document = SimpleDocTemplate(str(pdf_path))

    story = [
        Paragraph(title, styles["Heading1"]),
        Paragraph(content.replace("\n", "<br/>"), styles["BodyText"])
    ]

    document.build(story)

    return str(pdf_path)