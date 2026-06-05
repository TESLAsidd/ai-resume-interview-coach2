def get_resume_improvement_prompt(
    resume_text,
    job_description
):

    return f"""
You are an expert resume writer.

Resume:
{resume_text}

Job Description:
{job_description}

Tasks:

1. Identify weak resume sections.
2. Rewrite them professionally.
3. Add stronger action verbs.
4. Suggest measurable achievements.
5. Suggest missing keywords.

Return in markdown format.
"""
