from octochains.base import Agent


class TechnicalInterviewer(Agent):

    def __init__(self, llm_callable):
        super().__init__(
            role="Senior Technical Interviewer",
            goal="Evaluate technical depth, projects, skills, and interview readiness.",
            input_description="""
            Resume content.

            Provide:
            1. Technical Skill Score (0-100)
            2. Strongest Technical Area
            3. Weakest Technical Area
            4. Missing Projects
            5. Five Likely Interview Questions
            """,
            llm_callable=llm_callable
        )

    def execute(self, problem_data: str):
        prompt = self._build_prompt(problem_data)
        return self.llm_callable(prompt)
