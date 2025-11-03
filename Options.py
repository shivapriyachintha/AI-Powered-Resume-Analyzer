import streamlit as st

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

def run():
    # Background and styling
    st.markdown("""
        <style>
        html, body, [data-testid="stAppViewContainer"], section.main {
            background-image: url('https://images.unsplash.com/photo-1635254216305-fad20e1ac9c0?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        .stButton > button {
            background-color: white !important;
            color: #14213d !important;
            border: 1px solid #14213d !important;
            border-radius: 8px;
            font-weight: bold;
            padding: 0.6em 1.2em;
            font-size: 16px;
            margin: 10px 0;
        }
        .stButton > button:hover {
            background-color: #f0f0f0 !important;
            color: #000 !important;
            transform: scale(1.01);
        }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("<h1 style='text-align: center; color: #14213d;'>Resume AI Expert</h1>", unsafe_allow_html=True)

    # Go Back to Home
    if st.button("← Go Back to Home"):
        st.query_params.clear()
        st.session_state.clear()
        st.rerun()

    # Validate session state
    if "resume_bytes" not in st.session_state or "jd" not in st.session_state:
        st.warning("Please upload your resume and job description on the Home page.")
        st.stop()

    # Subtitle
    st.markdown("<h2 style='text-align: center; color: #14213d;'>Select an Option</h2>", unsafe_allow_html=True)

    # Buttons
    if st.button("📝 Evaluate Resume", use_container_width=True):
        st.query_params["page"] = "evaluate"
        st.rerun()

    if st.button("📊 Match % & Missing Keywords", use_container_width=True):
        st.query_params["page"] = "match"
        st.rerun()

    if st.button("🛠️ Improve Resume", use_container_width=True):
        st.query_params["page"] = "improve"
        st.rerun()

    if st.button("💼 Skills to Improve", use_container_width=True):
        st.query_params["page"] = "skills"
        st.rerun()

    if st.button("🔍 Find Jobs", use_container_width=True):
        st.query_params["page"] = "find"
        st.rerun()