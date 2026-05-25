import streamlit as st
import pandas as pd
import plotly.express as px

from utils.api_client import (
    fetch_attendance
)

from components.cards import (
    render_metric_card
)


def render_attendance_page():

    st.title("📋 Attendance Analytics")

    st.caption(
        "Real-time attendance monitoring dashboard"
    )

    try:

        attendance_data = (
            fetch_attendance()
        )

        if isinstance(
            attendance_data,
            list
        ):

            attendance_df = pd.DataFrame(
                attendance_data
            )

            st.write("")

            # METRICS

            col1, col2, col3 = st.columns(3)

            with col1:

                render_metric_card(
                    "Total Records",
                    str(
                        len(attendance_df)
                    ),
                    "📊"
                )

            with col2:

                unique_people = (
                    attendance_df[
                        "person_name"
                    ].nunique()
                )

                render_metric_card(
                    "Unique People",
                    str(unique_people),
                    "👥"
                )

            with col3:

                today_records = len(
                    attendance_df[
                        attendance_df["date"]
                        ==
                        attendance_df["date"].max()
                    ]
                )

                render_metric_card(
                    "Today's Attendance",
                    str(today_records),
                    "✅"
                )

            st.write("")
            st.write("")

            # ATTENDANCE TREND

            st.subheader(
                "📈 Attendance Trend"
            )

            attendance_trend = (
                attendance_df
                .groupby("date")
                .size()
                .reset_index(
                    name="attendance_count"
                )
            )

            trend_fig = px.line(
                attendance_trend,
                x="date",
                y="attendance_count",
                markers=True
            )

            trend_fig.update_layout(
                height=450
            )

            st.plotly_chart(
                trend_fig,
                use_container_width=True
            )

            st.write("")
            st.write("")

            # PERSON DISTRIBUTION

            st.subheader(
                "👤 Attendance Distribution"
            )

            person_distribution = (
                attendance_df[
                    "person_name"
                ]
                .value_counts()
                .reset_index()
            )

            person_distribution.columns = [
                "person_name",
                "count"
            ]

            pie_fig = px.pie(
                person_distribution,
                names="person_name",
                values="count"
            )

            pie_fig.update_layout(
                height=500
            )

            st.plotly_chart(
                pie_fig,
                use_container_width=True
            )

            st.write("")
            st.write("")

            # RAW TABLE

            st.subheader(
                "🗂️ Attendance Records"
            )

            st.dataframe(
                attendance_df,
                use_container_width=True
            )

        else:

            st.warning(
                attendance_data["message"]
            )

    except Exception as error:

        st.error(error)