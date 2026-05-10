import streamlit as st

def init_session_state():
    """Initialize necessary session state variables."""
    if 'resume_text' not in st.session_state:
        st.session_state.resume_text = None
    if 'resume_analysis' not in st.session_state:
        st.session_state.resume_analysis = None
    if 'target_role' not in st.session_state:
        st.session_state.target_role = "General"
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'file_name' not in st.session_state:
        st.session_state.file_name = None

def reset_session_state():
    """Reset session state for a new upload."""
    st.session_state.resume_text = None
    st.session_state.resume_analysis = None
    st.session_state.chat_history = []
    st.session_state.file_name = None

def get_common_roles():
    """Return a list of common job roles."""
    return [
        "Software Engineer",
        "Data Scientist",
        "Machine Learning Engineer",
        "Frontend Developer",
        "Backend Developer",
        "Full Stack Developer",
        "DevOps Engineer",
        "Cloud Architect",
        "Product Manager",
        "Business Analyst",
        "Data Analyst",
        "UI/UX Designer",
        "Cybersecurity Analyst",
        "General / Other"
    ]
