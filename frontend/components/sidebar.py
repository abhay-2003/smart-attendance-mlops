import streamlit as st


def render_sidebar():

    st.sidebar.title("🤖 Smart Attendance")

    st.sidebar.caption(
        "Enterprise AI Platform"
    )

    st.sidebar.markdown("---")

    selected_page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Recognition",
            "Attendance",
            "MLOps"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        "FastAPI • MLflow • Kubernetes"
    )

    return selected_page