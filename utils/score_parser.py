import re


def extract_scores(text):

    resume_score = "N/A"
    interview_score = "N/A"
    hiring_score = "N/A"

    resume_match = re.search(
        r"Resume Score[:\s]+(\d+)",
        text,
        re.IGNORECASE
    )

    interview_match = re.search(
        r"Interview.*?Score[:\s]+(\d+)",
        text,
        re.IGNORECASE
    )

    hiring_match = re.search(
        r"Hiring.*?(\d+)",
        text,
        re.IGNORECASE
    )

    if resume_match:
        resume_score = resume_match.group(1)

    if interview_match:
        interview_score = interview_match.group(1)

    if hiring_match:
        hiring_score = hiring_match.group(1)

    return (
        resume_score,
        interview_score,
        hiring_score
    )
