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


# GLOBAL CUSTOM CSS

st.markdown(
    """
    <style>

    /* MAIN APP */

    .stApp {

        background: linear-gradient(
            135deg,
            #020617,
            #071226,
            #0F172A
        );

        color: #F8FAFC;
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"] {

        background: linear-gradient(
            180deg,
            #020617,
            #0F172A
        );

        border-right: 1px solid #1E293B;
    }

    section[data-testid="stSidebar"] * {

        color: #F8FAFC !important;
    }

    /* HEADINGS */

    h1, h2, h3, h4, h5, h6 {

        color: #FFFFFF !important;
    }

    /* TEXT */

    p, label, span {

        color: #E2E8F0;
    }

    /* MAIN CONTAINER */

    .block-container {

        padding-top: 2rem;

        padding-left: 2rem;

        padding-right: 2rem;
    }

    /* METRIC CARDS */

    div[data-testid="metric-container"] {

        background: rgba(
            15,
            23,
            42,
            0.85
        );

        border: 1px solid rgba(
            59,
            130,
            246,
            0.25
        );

        padding: 20px;

        border-radius: 18px;

        box-shadow: 0px 4px 20px rgba(
            0,
            0,
            0,
            0.3
        );
    }

    /* BUTTONS */

    .stButton > button {

        width: 100%;

        background: linear-gradient(
            90deg,
            #2563EB,
            #06B6D4
        );

        color: white;

        border: none;

        border-radius: 12px;

        padding: 0.75rem 1.5rem;

        font-weight: 700;

        font-size: 15px;

        transition: 0.3s ease;
    }

    .stButton > button:hover {

        transform: scale(1.02);

        background: linear-gradient(
            90deg,
            #1D4ED8,
            #0891B2
        );
    }

    /* FILE UPLOADER */

    section[data-testid="stFileUploader"] {

        background-color: rgba(
            15,
            23,
            42,
            0.9
        );

        border: 2px dashed #3B82F6;

        border-radius: 14px;

        padding: 1rem;
    }

    section[data-testid="stFileUploader"] * {

        color: #F8FAFC !important;
    }

    /* TEXT INPUT */

    .stTextInput input {

        background-color: rgba(
            15,
            23,
            42,
            0.9
        );

        color: white;

        border-radius: 10px;

        border: 1px solid #334155;
    }

    /* DATAFRAME */

    .stDataFrame {

        background-color: rgba(
            15,
            23,
            42,
            0.85
        );

        border-radius: 12px;
    }

    /* JSON OUTPUT */

    .stJson {

        background-color: rgba(
            15,
            23,
            42,
            0.9
        );

        border-radius: 12px;

        padding: 10px;
    }

    /* ALERT BOXES */

    .stSuccess,
    .stError,
    .stWarning,
    .stInfo {

        border-radius: 12px;
    }

    /* SCROLLBAR */

    ::-webkit-scrollbar {

        width: 8px;
    }

    ::-webkit-scrollbar-thumb {

        background: #334155;

        border-radius: 10px;
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