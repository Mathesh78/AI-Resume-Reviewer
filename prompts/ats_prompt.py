ATS_PROMPT = """
You are an ATS (Applicant Tracking System) expert.

Analyze the following resume.

Resume Context:
{context}

Provide:

1. ATS Score out of 100
2. Resume Strengths
3. Resume Weaknesses
4. Missing Keywords
5. Formatting Issues
6. Actionable Suggestions

Return the result in proper markdown.
"""