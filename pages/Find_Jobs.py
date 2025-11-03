import streamlit as st
from PyPDF2 import PdfReader
import io
from utils import get_gemini_response

def run():
    # Background style
    st.markdown("""
        <style>
        html, body, [data-testid="stAppViewContainer"], section.main {
            background-image: url('https://images.unsplash.com/photo-1635254216305-fad20e1ac9c0?w=600&auto=format&fit=crop&q=60');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .stButton>button {
            background-color: white !important;
            color: black !important;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.4em 1.2em;
            border: 1px solid #999;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Heading
    st.markdown("<h1 style='text-align: center; color: #14213d;'>Resume AI Expert</h1>", unsafe_allow_html=True)

    # Back to Options
    if st.button("← Go Back to Options"):
        st.query_params["page"] = "options"
        st.rerun()

    # Session check
    if "resume_bytes" not in st.session_state or "jd" not in st.session_state:
        st.warning("Please upload your resume and job description on the Home page.")
        st.stop()

    # Extract text from PDF
    try:
        reader = PdfReader(io.BytesIO(st.session_state.resume_bytes))
        resume_text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    except:
        st.error("Couldn't extract text from PDF.")
        st.stop()

    job_description = st.session_state.jd

    # Prompt to Gemini
    prompt = """
    You are a smart job search assistant. Based on the user's resume and job description:
    - Extract the key job roles, skills, and technologies.
    - Generate a list of 5 to 8 job search keyword phrases useful on job portals like LinkedIn, Naukri, and Glassdoor.
    - Avoid any explanation or intro. Just give clean bullet points with search phrases only.
    """

    gemini_output = get_gemini_response(prompt, [resume_text], job_description)

    # Display Gemini output (raw)
    if not gemini_output:
        st.warning("No search terms were generated. Please check your input or try again.")
        return

    search_terms = [line.strip("-• ") for line in gemini_output.strip().split("\n") if line.strip()]
    
    if not search_terms:
        st.warning("No valid search keywords found.")
        return

    # Display Result
    st.markdown("<h3 style='color: #003049;'>🎯 Top Job Search Phrases:</h3>", unsafe_allow_html=True)
    for term in search_terms:
        st.markdown(f"🔹 **{term}**")
        portals = {
            "LinkedIn": "https://www.linkedin.com/jobs/search/?keywords=" + term.replace(" ", "%20"),
            "Glassdoor": "https://www.glassdoor.co.in/Job/jobs.htm?sc.keyword=" + term.replace(" ", "%20"),
            "Naukri": "https://www.naukri.com/" + "-".join(term.lower().split()) + "-jobs"
        }
        for name, url in portals.items():
            st.markdown(f"- [{name} Jobs]({url})", unsafe_allow_html=True)
        st.markdown("---")