import streamlit as st
import pandas as pd
import plotly.express as px

from components.cards import (
    render_metric_card
)

from utils.api_client import (
    check_api_health
)


def render_dashboard():

    st.title(
        "🤖 Smart Attendance AI Platform"
    )

    st.caption(
        "Enterprise MLOps Face Recognition System"
    )

    st.write("")

    # BACKEND HEALTH CHECK

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

    # METRIC CARDS

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        render_metric_card(
            title="Dataset Size",
            value="100",
            icon="🧠"
        )

    with col2:

        render_metric_card(
            title="Recognition Model",
            value="FaceNet",
            icon="🤖"
        )

    with col3:

        render_metric_card(
            title="Pipeline Status",
            value="Active",
            icon="⚡"
        )

    with col4:

        render_metric_card(
            title="Backend API",
            value="Online",
            icon="🟢"
        )

    st.write("")
    st.write("")

    # MLOPS PIPELINE

    st.subheader(
        "⚙️ MLOps Workflow Pipeline"
    )

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

    # ANALYTICS SECTION

    st.subheader(
        "📈 Attendance Analytics"
    )

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

        height=500,

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(

        fig,

        use_container_width=True
    )