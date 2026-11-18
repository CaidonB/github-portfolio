
import streamlit as st
from ollama import Client, ResponseError
from httpx import TimeoutException

st.set_page_config(page_title="AI Interview Coach")

MODEL = "llama3.2:1b"
client = Client(timeout=120)

#Communicate with Ollama and handle possible errors
def ask_ai(messages):
	try:
		response = client.chat(model=MODEL, messages=messages)
		result = (response.message.content or "").strip()

		if not result:
			st.error("The AI returned an empty response. Please try again.")
			return None
		
		return result
	
	except ConnectionError:
		st.error("Cannot connect to Ollama. Please start Ollama and try again.")

	except ResponseError as error:
		if error.status_code == 404:
			st.error(
				f"AI model '{MODEL}' was not found."
				f"Run 'ollama pull {MODEL}' in Git Bash."
			)
		else:
			st.error("Ollama could not complete the request. Please try again.")

	except TimeoutException:
		st.error("The AI request took too long. Please try again.")

	except Exception as error:
		st.error("An unexpected error occurred. Check the terminal for details.")
		print(f"Unexpected AI error: {error}")

	return None


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
        question = ask_ai([
            {
                "role": "system",
                "content": "You are a job interviewer. Ask exactly one interview question without giving the answer."
            },
            {
                "role": "user",
                "content": f"Generate a {category.lower()} interview question."
            }
        ])

        if question:
            st.session_state.question = question
            st.session_state.feedback = ""
            st.session_state.answer = ""

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
                feedback = ask_ai([
                    {
                        "role": "system",
                        "content": (
                            "You are an interview coach. Evaluate the candidate's answer. "
                            "Provide brief feedback with three sections: Strengths, "
                            "Weaknesses, and Suggestions for Improvement. "
                            "Keep your feedback under 150 words. "
                            "Do not invent experiences or accomplishments for the candidate."
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Interview Question: {st.session_state.question}\n\n"
                            f"Candidate Answer: {st.session_state.answer}"
                        )
                    }
                ])

                if feedback:
                    st.session_state.feedback = feedback

# Display AI feedback
if st.session_state.feedback:
    st.subheader("AI Feedback")
    st.write(st.session_state.feedback)
