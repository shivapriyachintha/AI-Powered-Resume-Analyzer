import streamlit as st
from utils import input_pdf_setup, get_gemini_response


def run():
    st.markdown("""
        <style>
        html, body, [data-testid="stAppViewContainer"], section.main {
            background-image: url('https://images.unsplash.com/photo-1635254216305-fad20e1ac9c0?w=600&auto=format&fit=crop&q=60');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        .stButton > button {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        padding: 0.6em 1.2em !important;
        font-size: 16px !important;
        border-radius: 8px !important;
        }
        .stButton > button:hover {
        background-color: #f0f0f0 !important;
        transform: scale(1.02);
        }
        </style>
    """, unsafe_allow_html=True,
    )

    st.markdown("<h2 style='text-align: center;'>📋 Resume Evaluation</h2>", unsafe_allow_html=True)

    if st.button("← Go Back to Options"):
        st.query_params["page"] = "options"
        st.rerun()

    if "resume_bytes" in st.session_state and "jd" in st.session_state:
        pdf_content = input_pdf_setup(st.session_state.resume_bytes)
        prompt = """
        You are an experienced Technical Human Resource Manager. Review the resume against
        the job description and give a detailed evaluation highlighting strengths and weaknesses of the
        applicant with respect to the role.
        """
        result = get_gemini_response(prompt, pdf_content, st.session_state.jd)
        st.write(result)
    else:
        st.warning("Resume or Job Description not found. Please go back to the Home page.")