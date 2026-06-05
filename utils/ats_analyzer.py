def get_ats_prompt(resume_text):

    return f"""
Analyze this resume for Applicant Tracking Systems (ATS).

Resume:
{resume_text}

Return EXACTLY in this format:

ATS Score: <number>

Missing Keywords:
- keyword1
- keyword2
- keyword3

Resume Issues:
- issue1
- issue2
- issue3

Improvement Suggestions:
- suggestion1
- suggestion2
- suggestion3
"""
