PROJECT_EXTRACTION_PROMPT = """
Extract every project from the resume.

Resume:

{context}

For every project provide:

Project Name

Description

Technologies Used

Responsibilities

Key Features

Return in markdown.
"""