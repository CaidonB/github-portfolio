AI Interview Coach READ ME





Project Overview:



This Project is a Python Application that is designed for users to prepare for job interviews by generating practice questions and being provided feedback on their responses with AI.



The application uses Streamlit for the UI and Ollama to run Llama 3.2 AI model locally. This project allows users too use the application with an API key or Paid AI service.





Features:



* Interview Category Selection: Users can choose between 3 different types of Interview Questions; General, Behavioral and Technical.



* Custom Interview Topics: Users can specify the topic for both Technical or Behavioral interview questions.



* AI Question Generation: The Application will generate a interview question using Llama 3.2 model.



* Written Answer Submission: Users can enter a response too the Interview Question.



* AI-Generated Feedback: The AI will evaluate the response input from user and provide feedback on strengths, weaknesses, and suggestions for improvement on the response.



* Input Validation and Error Handling: Displays messages with missing answers, Unavaiable AI model, or a connection error occurs.





Technologies Used:



* Python
* Streamlit
* Ollama
* Llama 3.2 (1B)
* Git and GitHub



Installation Instructions



The application runs locally and requires Python and Ollama.



1\. Install Python



Download and install Python from https://www.python.org/downloads/



2\. Install Ollama



Download and install Ollama from https://ollama.com/download



3\. Download the AI Model



Open a terminal and enter:



ollama pull llama3.2:1b



4\. Download the Project



Clone the GitHub repository:



git clone https://github.com/CaidonB/github-portfolio.git



Navigate to the project folder:



cd github-portfolio/ai-interview-coach



5\. Create a Virtual Environment



Create a Python virtual environment:



python -m venv .venv



Activate it in Git Bash on Windows:



source .venv/Scripts/activate



6\. Install Required Packages



Install the required Python dependencies:



python -m pip install -r requirements.txt





Usage Guide:



1. Make sure Ollama is running on your computer.



2\. Open a terminal in the ai-interview-coach folder and activate the Python virtual environment.



3\. Launch the application: python -m streamlit run app.py



4\. The application will open in your web browser.



5\. Select an interview category: General, Behavioral, or Technical.



6\. Optionally enter a specific topic for Technical or Behavioral interviews.



7\. Click Generate Interview Question.



8\. Type an answer in the provided text box.



9\. Click Submit Answer to receive AI-generated feedback.



10\. Review the feedback and generate additional questions to continue practicing.





\## Screenshots



\### Application Interface



!\[Application Interface](screenshots/Interface.png)



\### AI Question Generation



!\[AI Question Generation](screenshots/Question.png)



\### AI Feedback



!\[AI Feedback](screenshots/Feedback.png)

Testing:



* The application has been manually tested for:



* Interview question generation



* Answer submission and AI feedback



* Empty answer validation



* Changing interview categories



* Generating additional questions



* Missing AI model handling



* Ollama connection error handling



Additional test results are documented in TESTING.md.





Future Enhancements:



* Potential improvements to the application include:



* Saving previous interview questions and answers



* Tracking user performance across practice sessions



* Adding difficulty levels for interview questions



* Supporting voice-based interview practice



* Providing more detailed technical interview evaluations





Conclusion:



The AI Interview Coach demonstrates the use of AI-assisted software development to create a practical application for interview preparation. ChatGPT was used throughout the development process to assist with requirements analysis, software implementation, debugging, testing, and documentation.

