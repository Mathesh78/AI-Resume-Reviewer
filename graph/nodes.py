from langchain_core.messages import AIMessage

from graph.state import State
from models.llm import llm

from tools.resume_tools import (
    retrieve_resume,
    get_full_resume,
    validate_resume,
    resume_statistics,
    get_full_job_description,
)



# -----------------------------------------
# Summary
# -----------------------------------------

def summary_node(state: State):

    question = state["messages"][-1].content

    response = retrieve_resume(question)

    return {

        "answer": response,

        "messages": [

            AIMessage(content=response)

        ]

    }


# -----------------------------------------
# ATS
# -----------------------------------------

def ats_node(state: State):

    resume = get_full_resume()

    validation = validate_resume(resume)

    statistics = resume_statistics(resume)

    prompt = f"""
You are an expert ATS Resume Reviewer.

Below is the candidate's resume.

=========================
Resume
=========================

{resume}

=========================
Resume Validation
=========================

{validation}

=========================
Resume Statistics
=========================

{statistics}

Generate a detailed ATS Report.

Include the following sections:

1. Overall ATS Score (0-100)

2. Section Scores

- Formatting
- Skills
- Projects
- Experience
- Education

3. Resume Strengths

4. Resume Weaknesses

5. Missing Keywords

6. Missing Skills

7. Suggestions to improve ATS score

8. Final Verdict
"""

    response = llm.invoke(prompt)

    return {

        "answer": response.content,

        "messages": [

            AIMessage(content=response.content)

        ]

    }


# -----------------------------------------
# Interview
# -----------------------------------------

def interview_node(state: State):

    resume = get_full_resume()

    prompt = f"""
You are an interview preparation assistant.

Candidate Resume

{resume}

Generate:

1. 10 Technical Questions

2. 5 HR Questions

3. Answers

4. Difficulty Level

5. Interview Tips
"""

    response = llm.invoke(prompt)

    return {

        "answer": response.content,

        "messages": [

            AIMessage(content=response.content)

        ]

    }


# -----------------------------------------
# Career
# -----------------------------------------

def career_node(state: State):

    resume = get_full_resume()

    prompt = f"""
You are an experienced career mentor.

Candidate Resume

{resume}

Generate:

1. Career Summary

2. Strongest Skills

3. Missing Skills

4. Recommended Certifications

5. Learning Roadmap (30 Days)

6. Suitable Job Roles

7. Future Career Path
"""

    response = llm.invoke(prompt)

    return {

        "answer": response.content,

        "messages": [

            AIMessage(content=response.content)

        ]

    }

def match_node(state: State):

    resume = get_full_resume()

    job_description = get_full_job_description()

    prompt = f"""
You are an ATS Resume Matcher.

Compare the Resume with the Job Description.

====================
Resume
====================

{resume}

====================
Job Description
====================

{job_description}

Generate a professional report.

Include:

1. Overall Match Score (0-100)

2. Matching Skills

3. Missing Skills

4. Matching Technologies

5. Missing Keywords

6. Experience Match

7. Education Match

8. Strengths

9. Weaknesses

10. Suggestions to improve Resume

11. Final Verdict
"""

    response = llm.invoke(prompt)

    return {

        "answer": response.content,

        "messages": [

            AIMessage(content=response.content)

        ]

    }