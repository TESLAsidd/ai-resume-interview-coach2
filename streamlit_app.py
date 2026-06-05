import streamlit as st
import tempfile
import shutil


from utils.resume_parser import extract_text_from_pdf

from utils.score_parser import extract_scores
from utils.interview_generator import get_interview_prompt

from utils.ats_analyzer import get_ats_prompt
from utils.job_matcher import calculate_match
from utils.cover_letter_generator import get_cover_letter_prompt
from utils.pdf_generator import create_report_pdf
from utils.resume_improver import get_resume_improvement_prompt


from octochains.engine import Engine
from llm import call_llama

from agents.hr_recruiter import HRRecruiter
from agents.technical_interviewer import TechnicalInterviewer
from agents.hiring_manager import HiringManager
from agents.communication_coach import CommunicationCoach

from aggregator.career_mentor import CareerMentor

st.sidebar.title("AI Career Accelerator")

st.sidebar.markdown("""
### Features

✓ Resume Analysis

✓ ATS Optimization

✓ Job Matching

✓ Interview Preparation

✓ Resume Improvement

✓ Cover Letter Generator

✓ PDF Export
""")
st.set_page_config(
    page_title="AI Resume & Interview Coach",
    page_icon="📄",
    layout="wide"
)

st.title("🚀 AI Career Accelerator")

st.caption(
    "Resume Analysis • ATS Optimization • Interview Preparation • Cover Letter Generation"
)

analysis_mode = st.radio(
    "Analysis Mode",
    ["Quick", "Expert"]
)
job_description = st.text_area(
    "Paste Job Description",
    height=250
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        shutil.copyfileobj(uploaded_file, tmp)
        pdf_path = tmp.name

    try:

        resume_text = extract_text_from_pdf(pdf_path)
        match_score, found_skills, missing_skills = calculate_match(
            resume_text,
            job_description
        )

        st.success("Resume uploaded successfully!")

        st.subheader("Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )

        if st.button("Analyze Resume"):

            # ==================================================
            # QUICK MODE
            # ==================================================
            if analysis_mode == "Quick":

                with st.spinner("Running quick analysis..."):

                    quick_prompt = f"""
                    Analyze this resume.

                    Resume:
                    {resume_text}

                    Provide EXACTLY in this format:

                    Resume Score: <number>

                    Interview Score: <number>

                    Hiring Potential: <number>

                    Top Strengths:
                    - point 1
                    - point 2
                    - point 3

                    Top Weaknesses:
                    - point 1
                    - point 2
                    - point 3

                    Missing Skills:
                    - skill 1
                    - skill 2
                    - skill 3

                    Recommended Skills:
                    - skill 1
                    - skill 2
                    - skill 3

                    30-Day Improvement Plan:
                    - step 1
                    - step 2
                    - step 3
                    """

                    response = call_llama(quick_prompt)

                    ats_prompt = get_ats_prompt(resume_text)

                    ats_report = call_llama(ats_prompt)

                    interview_prompt = get_interview_prompt(resume_text)

                    interview_questions = call_llama(interview_prompt)
                    improvement_prompt = get_resume_improvement_prompt(
                        resume_text,
                        job_description
                    )

                    improvement_report = call_llama(
                        improvement_prompt
                    )
                    cover_letter_prompt = get_cover_letter_prompt(
                        resume_text,
                        job_description
                    )

                    cover_letter = call_llama(
                        cover_letter_prompt
                    )

                    full_report = (
                        str(response)
                        + "\n\n"
                        + str(ats_report)
                        + "\n\n"
                        + str(interview_questions)
                        + "\n\n"
                        + str(improvement_report)
                        + "\n\n"
                        + str(cover_letter)
                    )

                    create_report_pdf(
                        full_report,
                        "career_report.pdf"
                    )
                    import os

                    st.write("PDF Exists:", os.path.exists(
                        "career_report.pdf"))

                st.success("Quick Analysis Complete!")
                st.divider()

                resume_score, interview_score, hiring_score = extract_scores(
                    response)

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    label="📄 Resume Score",
                    value=resume_score
                )

                col2.metric(
                    label="🎯 Interview Score",
                    value=interview_score
                )

                col3.metric(
                    label="💼 Hiring Potential",
                    value=hiring_score
                )
                st.subheader("Job Match Analysis")

                st.metric("Match Score", f"{match_score}%")

                st.write("### Found Skills")
                for skill in found_skills:
                    st.success(f"✓ {skill}")

                st.write("### Missing Skills")
                for skill in missing_skills:
                    st.error(f"✗ {skill}")
                tab1, tab2, tab3, tab4, tab5 = st.tabs([
                    "Career Report",
                    "ATS Analysis",
                    "Interview Questions",
                    "Resume Improvements",
                    "Cover Letter"
                ])

                with tab1:
                    st.subheader("Quick Career Report")
                    st.markdown(response)
                with tab2:
                    st.subheader("ATS Analysis")
                    st.markdown(ats_report)
                with tab3:
                    st.subheader("Interview Preparation")
                    st.markdown(interview_questions)
                with tab4:
                    st.subheader("Resume Improvement Suggestions")
                    st.markdown(improvement_report)
                with tab5:
                    st.subheader("Cover Letter")
                    st.markdown(cover_letter)

                st.divider()

                with open("career_report.pdf", "rb") as pdf_file:

                    st.download_button(
                        label="📄 Download PDF Report",
                        data=pdf_file,
                        file_name="career_report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            # ==================================================
            # EXPERT MODE
            # ==================================================
            else:

                progress = st.progress(0)

                st.write("✅ Step 1/5 Resume Parsed")
                progress.progress(20)

                agents = [
                    HRRecruiter(call_llama),
                    TechnicalInterviewer(call_llama),
                    HiringManager(call_llama),
                    CommunicationCoach(call_llama)
                ]

                st.write("✅ Step 2/5 Running Expert Analysis")
                progress.progress(40)

                aggregator = CareerMentor(call_llama)

                engine = Engine(
                    agents=agents,
                    aggregator=aggregator
                )

                report = engine.run(
                    problem_data=resume_text,
                    show_log=False
                )
                create_report_pdf(
                    str(report.consensus),
                    "career_report.pdf"
                )

                st.write("✅ Step 3/5 Generating Report")
                progress.progress(70)

                st.write("✅ Step 4/5 Finalizing")
                progress.progress(90)

                progress.progress(100)

                st.success("Expert Analysis Complete!")

                report_text = str(report.consensus)

                resume_score, interview_score, hiring_score = extract_scores(
                    report_text)

                col1, col2, col3 = st.columns(3)

                col1.metric("Resume Score", resume_score)
                col2.metric("Interview Score", interview_score)
                col3.metric("Hiring Potential", hiring_score)
                st.subheader("Job Match Analysis")

                st.metric("Match Score", f"{match_score}%")

                st.write("### Found Skills")
                st.write(found_skills)

                st.write("### Missing Skills")
                st.write(missing_skills)

                st.subheader("Final Career Report")

                st.markdown(report.consensus)

                st.divider()

                with open("career_report.pdf", "rb") as pdf_file:

                    st.download_button(
                        label="📄 Download PDF Report",
                        data=pdf_file,
                        file_name="career_report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

    except Exception as e:

        st.error(f"Error: {e}")
