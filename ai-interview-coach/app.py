import streamlit as st
from ollama import chat

st.set_page_config(page_title="AI Interview Coach")

st.title("AI Interview Coach")
st.write("Practice job interview questions and receive AI-generated feedback.")

st.subheader("Interview Settings")

category = st.selectbox(
    "Select an interview category:",
    ["General", "Behavioral", "Technical"]
)

if st.session_state.get("last_category") != category:
    st.session_state.question = ""
    st.session_state.last_category = category

if st.button("Generate Interview Question"):
    with st.spinner("Generating question..."):
        try:
            response = chat(
                model="llama3.2:1b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a job interviewer. Ask exactly one interview question without giving the answer."
                    },
                    {
                        "role": "user",
                        "content": f"Generate a {category.lower()} interview question."
                    }
                ]
            )
            st.session_state.question = response.message.content

        except Exception as error:
            st.error(f"Unable to generate question: {error}")

if st.session_state.question:
    st.subheader("Interview Question")
    st.write(st.session_state.question)
