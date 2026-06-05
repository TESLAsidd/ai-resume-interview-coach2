def get_cover_letter_prompt(
    resume_text,
    job_description
):

    return f"""
You are an expert career coach.

Resume:
{resume_text}

Job Description:
{job_description}

Write a professional cover letter.

Requirements:

1. Tailor it to the job description.
2. Highlight relevant skills.
3. Mention key projects.
4. Keep it under 400 words.
5. Sound professional and natural.

Return only the cover letter.
"""
