SKILL_EXTRACTION_PROMPT = """
Extract every skill mentioned in this resume.

Resume:

{context}

Group them into:

Programming Languages

Frameworks

Databases

Cloud

AI/ML

Testing

DevOps

Tools

Soft Skills

Return as bullet points.
"""