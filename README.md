# Text File Chatbot

This Streamlit app allows you to upload and interact with text files up to 200MB in size.  You can ask questions about the content of the file and receive answers, effectively turning your text file into a conversational chatbot.

## Features

* **Large File Support:** Handles text files up to 200MB, making it suitable for substantial documents, books, or code repositories.
* **Chat-Based Interaction:** Ask questions about the content of your uploaded file in a conversational manner. The app uses open AI language processing to understand your queries and provide relevant answers.
* **Easy to Use:**  Simply upload your text file and start chatting!  The interesting Streamlit interface makes it easy for anyone to use.
* **Privacy Focused:** Your uploaded files are processed and used only within your current session.  No data is stored or shared.  

## How to Use

1. **Upload:**  Click the "Browse files" button to select the text file you want to analyze.  The app supports various text file formats (e.g., `.txt`, `.csv`, `.md`, `.py`).
2. **Chat:** Once the file is uploaded, a chat interface will appear. Type your questions or requests in the chat box and press Enter.
3. **Review Answers:** The app will process your query and provide an answer based on the content of the uploaded file.
4. **Continue Chatting:** You can continue asking questions and refining your queries to explore the information in your text file.

## Technical Details 

* **Powered by:**  Streamlit, LangChain (For text processing and chatbot functionality).
* **Model:**  Uses OpenAI's default gpt-3.5-turbo-instruct model.
* **File Size Limit:** 200MB.

## Local Development

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/NagaVemprala/01_Streamlit.git](https://github.com/NagaVemprala/01_Streamlit.git)