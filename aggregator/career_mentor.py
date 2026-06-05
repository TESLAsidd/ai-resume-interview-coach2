from octochains.base import Aggregator


class CareerMentor(Aggregator):

    def __init__(self, llm_callable):
        super().__init__(
            role="Senior Career Mentor",
            goal="Combine all expert evaluations into a single actionable career improvement roadmap.",
            llm_callable=llm_callable
        )

    def execute(self, agent_reports: dict):

        compiled_reports = self._format_reports(agent_reports)

        prompt = f"""
You are a {self.role}.

GOAL:
{self.goal}

EXPERT REPORTS:
{compiled_reports}

Create a final report with:

1. Overall Resume Score (0-100)
2. Interview Readiness Score (0-100)
3. Top Strengths
4. Top Weaknesses
5. Recommended Projects
6. Recommended Skills To Learn
7. 30-Day Improvement Plan
8. Final Hiring Potential Assessment
"""

        return self.llm_callable(prompt)
