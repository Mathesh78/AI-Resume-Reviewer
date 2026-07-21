SUMMARY_PROMPT = """
You are an expert resume reviewer.

Use ONLY the resume context below.

Resume Context:
{context}

Generate a professional summary containing:

1. Candidate Profile
2. Education
3. Experience
4. Technical Skills
5. Projects
6. Strengths

Keep the summary within 8-10 lines.

If information is missing, say "Not Mentioned".

Return only the summary.
"""