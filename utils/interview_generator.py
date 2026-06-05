def get_interview_prompt(resume_text):

    return f"""
    You are a senior technical interviewer.

    Resume:
    {resume_text}

    Generate:

    TECHNICAL QUESTIONS:
    10 personalized technical questions

    HR QUESTIONS:
    5 personalized HR questions

    PROJECT QUESTIONS:
    5 project-based questions

    Return in clean markdown format.
    """
