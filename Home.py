import streamlit as st
from utils import input_pdf_setup

# Page config
st.set_page_config(page_title="Resume AI Expert", layout="centered")

st.markdown(
    """
    <style>
    /* Hide sidebar navigation */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* Hide entire sidebar */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Hide sidebar collapse button */
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* Remove sidebar space and expand main content */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Make main content full width */
    .main .block-container {
        max-width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Styling
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], section.main {
        background-image: url('https://images.unsplash.com/photo-1635254216305-fad20e1ac9c0?w=600&auto=format&fit=crop&q=60') !important;
        background-size: cover !important;
        background-position: center;
        background-repeat: no-repeat;
    }
    .stTextArea label, .stFileUploader label {
        color: #14213d !important;
        font-weight: 600;
    }
    .stTextArea textarea, .stFileUploader {
        background-color: #ffffff !important;
        border: 1px solid #9db3c8;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #3a86ff;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-size: 16px;
        margin-top: 1rem;
    }
    .stButton>button:hover {
        background-color: #265df2 !important;
        transform: scale(1.02);
    }
    header {
        background-color: #f2f2f2 !important;
        padding: 10px;
    }
    header * {
        color: #14213d !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Header title
if st.query_params.get("page", None) is None:
    st.markdown("<h1 style='color:#14213d; text-align:center;'>Resume AI Expert</h1>", unsafe_allow_html=True)

# 🔁 Get current page from query parameters
page = st.query_params.get("page", None)

if page and page != "Home":
    if "resume_bytes" not in st.session_state or "jd" not in st.session_state:
        st.query_params.clear()
        st.rerun()

# ✅ Always show form if query param is empty or equals "Home"
if not page or page == "Home":
    # Clear query params if "Back to Home" was clicked
    if "page" in st.query_params:
        st.query_params.clear()
        st.rerun()

    # Resume upload and JD input
    jd = st.text_area("Paste the Job Description here 👇", key="jd_input")
    uploaded_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])

    if st.button("Submit"):
        if not jd or not uploaded_file:
            st.warning("Please upload both resume and job description.")
        else:
            st.session_state.resume_bytes = uploaded_file.read()
            st.session_state.jd = jd
            st.query_params["page"] = "options"
            st.rerun()

# ✅ Show other pages if resume + jd exist in session state
elif "resume_bytes" in st.session_state and "jd" in st.session_state:
    if page == "options":
        import Options
        Options.run()
    elif page == "evaluate":
        from pages import Evaluation
        Evaluation.run()
    elif page == "match":
        from pages import Match
        Match.run()
    elif page == "improve":
        from pages import Improve
        Improve.run()
    elif page == "skills":
        from pages import Skills
        Skills.run()
    elif page == "find":
        from pages import Find_Jobs
        Find_Jobs.run()