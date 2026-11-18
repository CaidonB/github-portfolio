
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

# Initialize session state
if "question" not in st.session_state:
    st.session_state.question = ""

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "answer" not in st.session_state:
    st.session_state.answer = ""

# Reset when the interview category changes
if st.session_state.get("last_category") != category:
    st.session_state.question = ""
    st.session_state.feedback = ""
    st.session_state.answer = ""
    st.session_state.last_category = category

# Generate interview question
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
            st.session_state.feedback = ""
            st.session_state.answer = ""

        except Exception as error:
            st.error(f"Unable to generate question: {error}")

# Display question and accept answer
if st.session_state.question:
    st.subheader("Interview Question")
    st.write(st.session_state.question)

    st.text_area(
        "Enter your answer:",
        key="answer",
        height=150
    )

    # Submit answer for AI evaluation
    if st.button("Submit Answer"):
        if not st.session_state.answer.strip():
            st.warning("Please enter an answer before submitting.")
        else:
            with st.spinner("Evaluating your answer..."):
                try:
                    response = chat(
                        model="llama3.2:1b",
                        messages=[
                            {
                                "role": "system",
                                "content": "You are an interview coach. Evaluate the candidate's answer. Provide brief feedback with three sections: Strengths, Weaknesses, and Suggestions for Improvement. Keep your feedback under 150 words. Do not invent experiences or accomplishments for the candidate."
                            },
                            {
                                "role": "user",
                                "content": f"Interview Question: {st.session_state.question}\n\nCandidate Answer: {st.session_state.answer}"
                            }
                        ]
                    )

                    st.session_state.feedback = response.message.content

                except Exception as error:
                    st.error(f"Unable to evaluate answer: {error}")

# Display AI feedback
if st.session_state.feedback:
    st.subheader("AI Feedback")
    st.write(st.session_state.feedback)
