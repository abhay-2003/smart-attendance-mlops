import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
from requests.exceptions import ConnectionError

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Smart Attendance AI Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #0E1117;
        color: white;
    }

    .stApp {
        background: linear-gradient(
            to bottom right,
            #0E1117,
            #111827
        );
    }

    .metric-card {
        background: rgba(17, 25, 40, 0.75);
        border: 1px solid rgba(0, 255, 255, 0.2);
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0px 4px 30px rgba(0, 255, 255, 0.1);
    }

    .title-text {
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(
            to right,
            #00FFFF,
            #3B82F6
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle-text {
        color: #9CA3AF;
        font-size: 18px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🤖 Smart Attendance AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Face Recognition",
        "Attendance Logs",
        "MLOps Monitoring",
        "System Architecture"
    ]
)

# =========================================================
# DASHBOARD PAGE
# =========================================================

if page == "Dashboard":

    st.markdown(
        '<p class="title-text">Smart Attendance AI Platform</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle-text">Enterprise AI/ML MLOps System with FastAPI, MLflow, DVC, Docker & Kubernetes</p>',
        unsafe_allow_html=True
    )

    st.write("")

    # =====================================================
    # METRICS
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            """
            <div class="metric-card">
                <h3>Total Faces</h3>
                <h1>100</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="metric-card">
                <h3>Recognition Model</h3>
                <h1>FaceNet</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="metric-card">
                <h3>MLflow Runs</h3>
                <h1>Active</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            """
            <div class="metric-card">
                <h3>Backend API</h3>
                <h1>Online</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # =====================================================
    # SYSTEM WORKFLOW
    # =====================================================

    st.subheader("⚡ MLOps Workflow Pipeline")

    workflow_cols = st.columns(7)

    workflow_steps = [
        "Dataset",
        "DVC + S3",
        "Embeddings",
        "MLflow",
        "FastAPI",
        "Docker",
        "Kubernetes"
    ]

    for col, step in zip(workflow_cols, workflow_steps):

        with col:

            st.markdown(
                f'''
                <div class="metric-card">
                    <h4>{step}</h4>
                </div>
                ''',
                unsafe_allow_html=True
            )

    st.write("")
    st.write("")

    # =====================================================
    # SAMPLE ANALYTICS
    # =====================================================

    st.subheader("📊 Attendance Analytics")

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

    fig = px.line(
        analytics_data,
        x="Day",
        y="Attendance",
        markers=True,
        title="Weekly Attendance Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# FACE RECOGNITION PAGE
# =========================================================

elif page == "Face Recognition":

    st.title("🧠 Face Recognition")

    st.write(
        "Upload image for AI-powered recognition."
    )

    uploaded_file = st.file_uploader(
        "Upload Face Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button("Recognize Face"):

            with st.spinner("Processing AI Recognition..."):

                try:

                    files = {
                        "file": uploaded_file.getvalue()
                    }

                    response = requests.post(
                        "http://127.0.0.1:8000/recognize",
                        files=files
                    )

                    result = response.json()

                    st.success("Recognition Completed!")

                    st.json(result)

                except Exception as error:

                    st.error(error)

# =========================================================
# ATTENDANCE LOGS PAGE
# =========================================================

elif page == "Attendance Logs":

    st.title("📋 Attendance Logs")

    try:

        response = requests.get(
            "http://127.0.0.1:8000/attendance"
        )

        attendance_data = response.json()

        if len(attendance_data) > 0:

            attendance_df = pd.DataFrame(
                attendance_data
            )

            st.dataframe(
                attendance_df,
                use_container_width=True
            )

        else:

            st.warning("No attendance records found.")

    except Exception as error:

        st.error(error)

# =========================================================
# MLOPS MONITORING PAGE
# =========================================================

elif page == "MLOps Monitoring":

    st.title("⚙️ MLOps Monitoring Dashboard")

    st.markdown("""
    ### 🚀 Current MLOps Stack

    - ✅ DVC Dataset Versioning
    - ✅ AWS S3 Remote Storage
    - ✅ MLflow Experiment Tracking
    - ✅ FastAPI Backend
    - ✅ Real-Time Recognition
    - ✅ Streamlit Frontend
    - 🔄 Docker Containerization
    - 🔄 GitHub Actions CI/CD
    - 🔄 Kubernetes Deployment
    """)

    st.write("")

    st.info(
        "MLflow UI available at: http://127.0.0.1:5000"
    )

# =========================================================
# SYSTEM ARCHITECTURE PAGE
# =========================================================

elif page == "System Architecture":

    st.title("🏗️ Enterprise System Architecture")

    st.code(
        '''
Frontend (Streamlit)
        ↓
FastAPI Backend
        ↓
Recognition Engine
        ↓
Embedding Database
        ↓
Attendance Logs
        ↓
MLflow Tracking
        ↓
Docker
        ↓
Kubernetes
        ↓
AWS Deployment
        '''
    )

    st.write("")

    st.subheader("📦 Technology Stack")

    tech_stack = pd.DataFrame({
        "Layer": [
            "Frontend",
            "Backend",
            "AI Model",
            "MLOps",
            "Containerization",
            "Orchestration",
            "Cloud"
        ],
        "Technology": [
            "Streamlit",
            "FastAPI",
            "DeepFace + FaceNet",
            "MLflow + DVC",
            "Docker",
            "Kubernetes",
            "AWS"
        ]
    })

    st.table(tech_stack)