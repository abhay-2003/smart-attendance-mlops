import streamlit as st

from components.sidebar import (
    render_sidebar
)

from pages.dashboard import (
    render_dashboard
)

from pages.recognition import (
    render_recognition_page
)

from pages.attendance import (
    render_attendance_page
)

from pages.mlops import (
    render_mlops_page
)


# PAGE CONFIGURATION

st.set_page_config(
    page_title="Smart Attendance AI Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# GLOBAL STYLING

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #020617,
            #071226,
            #0F172A
        );
        color: white;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #020617,
            #0F172A
        );
        border-right: 1px solid #1E293B;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }

    p, label, div {
        color: white;
    }

    .stDataFrame {
        background-color: rgba(
            15,
            23,
            42,
            0.8
        );

        border-radius: 12px;
    }

    div[data-testid="metric-container"] {

        background-color: rgba(
            15,
            23,
            42,
            0.7
        );

        border: 1px solid rgba(
            59,
            130,
            246,
            0.2
        );

        padding: 20px;

        border-radius: 16px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# SIDEBAR NAVIGATION

selected_page = render_sidebar()


# PAGE ROUTING

if selected_page == "Dashboard":

    render_dashboard()


elif selected_page == "Recognition":

    render_recognition_page()


elif selected_page == "Attendance":

    render_attendance_page()


elif selected_page == "MLOps":

    render_mlops_page()