from octochains.base import Agent


class CommunicationCoach(Agent):

    def __init__(self, llm_callable):
        super().__init__(
            role="Professional Communication Coach",
            goal="Improve clarity, impact, grammar, and professional presentation.",
            input_description="""
            Resume content.

            Provide:
            1. Communication Score (0-100)
            2. Grammar Issues
            3. Weak Bullet Points
            4. Suggested Improvements
            5. Overall Presentation Quality
            """,
            llm_callable=llm_callable
        )

    def execute(self, problem_data: str):
        prompt = self._build_prompt(problem_data)
        return self.llm_callable(prompt)
