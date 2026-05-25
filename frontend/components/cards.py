import streamlit as st


def render_metric_card(
    title,
    value,
    icon="📊"
):

    st.markdown(
        f"""
        ### {icon} {title}

        ## {value}
        """
    )