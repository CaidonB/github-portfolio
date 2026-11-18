
import streamlit as st

st.set_page_config(page_title="AI Interview Coach")

st.title("AI Interview Coach")

st.write("Practice job interview questions and receive AI-generated feedback.")

st.subheader("Interview Settings")

category = st.selectbox(
    "Select an interview category:",
    ["General", "Behavioral", "Technical"]
)

st.write("Selected category:", category)
