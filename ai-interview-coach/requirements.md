AI Interview Coach Requirements Document



1. Project Overview

The AI Interview Coach will be a Python application and designed to help users/clients to prepare for job interviews. This application will allow the user too answer practice interview questions and the AI will generate feedback for their answers.



This application will be using Streamlit for the UI and Ollama to run the AI model locally too bypass the need for a API key.



2\. Functional Requirements

This AI Interview Coach will provide these functionalities:



1. Allow user to select an interview category like General, Behavioral, or Technical.
2. Generate questions based on the category selected using the AI model.
3. Allow the user/client too input responses to the questions.
4. The AI will analyze the submitted responses and provide feedback on the answers.
5. AI will provide suggestions on improvement based on answers too questions.
6. Allow the user to generate additional questions to continue practicing
7. Display error messages when the inputs required are missing or the AI model is not available.



3\. Non-Functional Requirements

This AI Interview Coach will provide these non-functionalities:



1. Application will be simple and user friendly.
2. Application will run on computer locally with Python, Streamlit, and Ollama installed.
3. Application will handle wrong inputs and errors and not crash.
4. The Applications source code will be organized and readable.
5. Application will provide feed back in a reasonable time frame, but this will be dependent on the hardware of the computer and AI model.



4\. Assumptions



1. Users will have access to a machine that is capable of running Python and a local AI model
2. Python, Streamlit, and Ollama will be installed and configured.
3. Users input will be written answers and not spoken responses.
4. Application will use some existing AI model rather then training a new model
5. An internet connection will be required for the initial installation and for the model download, but once done it will no longer.



5\. Project Scope



This project will be focused on developed a interview coach application powered with AI. The application will include category's for interviews to select from, question generation, a written answer submission, and feedback that is AI-generated



This Application will not include accounts, and type of voice recognition, videos, or hosting online.



The primary goal for this project is to create a function application with the assistance of AI in software development.

