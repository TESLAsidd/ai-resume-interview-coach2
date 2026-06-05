from utils.resume_parser import extract_text_from_pdf
from octochains.engine import Engine

from llm import call_llama

from agents.hr_recruiter import HRRecruiter
from agents.technical_interviewer import TechnicalInterviewer
from agents.hiring_manager import HiringManager
from agents.communication_coach import CommunicationCoach

from aggregator.career_mentor import CareerMentor


def main():

    resume_text = resume_text = extract_text_from_pdf("data/resume.pdf")
    agents = [
        HRRecruiter(call_llama),
        TechnicalInterviewer(call_llama),
        HiringManager(call_llama),
        CommunicationCoach(call_llama)
    ]

    aggregator = CareerMentor(call_llama)

    engine = Engine(
        agents=agents,
        aggregator=aggregator
    )

    report = engine.run(
        problem_data=resume_text,
        show_log=True
    )

    print("\n")
    print("=" * 80)
    print("FINAL CAREER REPORT")
    print("=" * 80)

    print(report.consensus)


if __name__ == "__main__":
    main()
