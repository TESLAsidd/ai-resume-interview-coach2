from octochains.base import Agent


class HiringManager(Agent):

    def __init__(self, llm_callable):
        super().__init__(
            role="Hiring Manager",
            goal="Determine whether the candidate should be hired for an internship or entry-level role.",
            input_description="""
            Resume content.

            Provide:
            1. Hiring Score (0-100)
            2. Candidate Strengths
            3. Candidate Risks
            4. Recommended Role
            5. Hire / Hold / Reject Decision
            """,
            llm_callable=llm_callable
        )

    def execute(self, problem_data: str):
        prompt = self._build_prompt(problem_data)
        return self.llm_callable(prompt)
