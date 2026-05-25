import streamlit as st
import plotly.express as px
import pandas as pd

from utils.api_client import recognize_face

from components.cards import (
    render_metric_card
)


def render_recognition_page():

    st.title("🧠 AI Face Recognition")

    st.caption(
        "Real-time FaceNet Recognition Engine"
    )

    st.write("")

    upload_col, info_col = st.columns(
        [1.2, 1]
    )

    with upload_col:

        uploaded_file = st.file_uploader(
            "Upload Face Image",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is not None:

            st.image(
                uploaded_file,
                use_container_width=True
            )

    with info_col:

        st.subheader(
            "⚙️ Recognition Pipeline"
        )

        st.info("1. Image Upload")

        st.info("2. Embedding Generation")

        st.info("3. Face Comparison")

        st.info("4. Confidence Analysis")

        st.info("5. Attendance Logging")

    st.write("")
    st.write("")

    if uploaded_file is not None:

        if st.button(
            "🚀 Run AI Recognition",
            use_container_width=True
        ):

            with st.spinner(
                "Running AI Recognition Pipeline..."
            ):

                try:

                    result = recognize_face(
                        uploaded_file
                    )

                    st.success(
                        "Recognition Completed"
                    )

                    st.write("")
                    st.write("")

                    # RESULT CARDS

                    col1, col2, col3 = st.columns(3)

                    with col1:

                        render_metric_card(
                            "Predicted Person",
                            result[
                                "predicted_person"
                            ],
                            "👤"
                        )

                    with col2:

                        render_metric_card(
                            "Confidence",
                            f"{result['confidence_percentage']}%",
                            "📈"
                        )

                    with col3:

                        render_metric_card(
                            "Status",
                            result["status"],
                            "✅"
                        )

                    st.write("")
                    st.write("")

                    # CONFIDENCE VISUALIZATION

                    st.subheader(
                        "📊 Confidence Analysis"
                    )

                    confidence_df = pd.DataFrame({

                        "Metric": [
                            "Confidence"
                        ],

                        "Value": [
                            result[
                                "confidence_percentage"
                            ]
                        ]
                    })

                    fig = px.bar(
                        confidence_df,
                        x="Metric",
                        y="Value",
                        text="Value"
                    )

                    fig.update_layout(
                        height=400
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True 
                    )

                    st.write("")
                    st.write("")

                    # DETAILED RESULTS

                    st.subheader(
                        "🗂️ Recognition Details"
                    )

                    st.json(result)

                except Exception as error:

                    st.error(error)