AI Interview Coach - Testing Documentation



1\. Testing Overview



The AI Interview Coach was manually tested to verify that its main features function correctly. Testing focused on user input validation, interview question generation, answer submission, and application behavior.



2\. Functional Testing



Test 1: Empty Answer Validation



Test Procedure:

1\. Generate an interview question.

2\. Leave the answer field empty.

3\. Click Submit Answer.



Expected Result:

The application should display a warning requesting that the user enter an answer.



Actual Result:

The application displayed the expected warning.



Status: PASS



Test 2: Generate Another Question



Test Procedure:

1\. Generate an interview question.

2\. Enter and submit an answer.

3\. Receive AI-generated feedback.

4\. Click Generate Interview Question again.



Expected Result:

The application should generate another question and clear the previous answer and feedback.



Actual Result:

The application generated another question and cleared the previous answer and feedback.



Status: PASS



Test 3: Change Interview Category



Test Procedure:

1\. Select the General interview category.

2\. Generate an interview question.

3\. Change the category to Technical.



Expected Result:

The application should clear the previous question, answer, and feedback, allowing the user to generate a question for the new category.



Actual Result:

The application cleared the previous information and allowed another question to be generated.



Status: PASS



3\. AI Functionality Testing



The application was also tested to verify that Ollama and Llama 3.2 could generate interview questions and evaluate written answers.



Question Generation: PASS



Answer Evaluation: PASS



Feedback Organization: PASS



The AI successfully generated interview questions and provided feedback identifying strengths, weaknesses, and suggestions for improvement.



4\. Testing Summary



All documented tests passed.



Additional testing will focus on handling unavailable AI models, improving error handling, and verifying the application's reliability before final submission.

