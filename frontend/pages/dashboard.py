import streamlit as st
import pandas as pd
import plotly.express as px

from components.cards import render_metric_card
from utils.api_client import check_api_health


def render_dashboard():

    st.title("🤖 Smart Attendance AI Platform")

    st.caption(
        "Enterprise MLOps Face Recognition System"
    )

    st.write("")

    try:

        health = check_api_health()

        st.success(
            f"Backend Connected • {health['message']}"
        )

    except Exception as error:

        st.error(
            f"Backend Connection Failed • {error}"
        )

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        render_metric_card(
            "Dataset Size",
            "100",
            "🧠"
        )

    with col2:

        render_metric_card(
            "Recognition Model",
            "FaceNet",
            "🤖"
        )

    with col3:

        render_metric_card(
            "Pipeline Status",
            "Active",
            "⚡"
        )

    with col4:

        render_metric_card(
            "Backend API",
            "Online",
            "🟢"
        )

    st.write("")
    st.write("")

    st.subheader("⚙️ MLOps Workflow Pipeline")

    workflow_steps = [
        "Dataset",
        "DVC",
        "Embeddings",
        "MLflow",
        "FastAPI",
        "Docker",
        "Kubernetes"
    ]

    workflow_cols = st.columns(
        len(workflow_steps)
    )

    for col, step in zip(
        workflow_cols,
        workflow_steps
    ):

        with col:

            st.info(step)

    st.write("")
    st.write("")

    st.subheader("📈 Attendance Analytics")

    analytics_data = pd.DataFrame({
        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri"
        ],

        "Attendance": [
            78,
            85,
            90,
            88,
            95
        ]
    })

    fig = px.area(
        analytics_data,
        x="Day",
        y="Attendance",
        markers=True
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )