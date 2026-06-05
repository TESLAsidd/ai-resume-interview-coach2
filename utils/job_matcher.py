import re


def calculate_match(resume_text, job_description):

    resume_lower = resume_text.lower()

    skills = [
        "python",
        "java",
        "c++",
        "sql",
        "mysql",
        "mongodb",
        "docker",
        "kubernetes",
        "aws",
        "azure",
        "react",
        "django",
        "flask",
        "git",
        "linux"
    ]

    found = []
    missing = []

    for skill in skills:

        if skill in job_description.lower():

            if skill in resume_lower:
                found.append(skill)
            else:
                missing.append(skill)

    total = len(found) + len(missing)

    if total == 0:
        score = 0
    else:
        score = round((len(found) / total) * 100)

    return score, found, missing
