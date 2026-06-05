from octochains.base import Agent


class HRRecruiter(Agent):

    def __init__(self, llm_callable):
        super().__init__(
            role="Senior HR Recruiter",
            goal="Evaluate the resume from a recruiter's perspective and identify weaknesses that could cause rejection.",
            input_description="""
            Resume content.

            Provide:
            1. ATS Score (0-100)
            2. Resume Strengths
            3. Resume Weaknesses
            4. Missing Keywords
            5. Probability of Shortlisting
            """,
            llm_callable=llm_callable
        )

    def execute(self, problem_data: str):
        prompt = self._build_prompt(problem_data)
        return self.llm_callable(prompt)
