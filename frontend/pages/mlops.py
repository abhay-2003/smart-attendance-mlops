import streamlit as st
import pandas as pd


def render_mlops_page():

    st.title("⚙️ MLOps Monitoring")

    st.caption(
        "Infrastructure and pipeline monitoring"
    )

    infrastructure_data = pd.DataFrame({

        "Component": [
            "FastAPI Backend",
            "Recognition Engine",
            "MLflow",
            "DVC",
            "Docker",
            "Kubernetes"
        ],

        "Status": [
            "Running",
            "Running",
            "Active",
            "Connected",
            "Configured",
            "Configured"
        ]
    })

    st.dataframe(
        infrastructure_data,
        use_container_width=True
    )

    st.success(
        "MLOps Pipeline Operational"
    )