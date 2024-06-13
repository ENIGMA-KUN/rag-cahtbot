# RAG-Powered Chatbot

This project is a Retrieval-Augmented Generation (RAG) powered chatbot that can answer questions based on the content of a provided PDF document. The chatbot uses various natural language processing (NLP) techniques to understand and respond to user queries by retrieving relevant information from the document.

## Features

- Extracts text from PDF documents
- Splits the text into manageable chunks
- Embeds the text chunks using HuggingFace embeddings
- Stores the embeddings in a vector store using FAISS
- Utilizes a conversational retrieval chain to handle user queries
- Provides a simple and interactive user interface using Streamlit

## Requirements

- Python 3.7+
- The following Python packages:

- pip install -r requirements.txt

Alternatively, you can install the packages individually:

pip install PyPDF2==3.0.0
pip install langchain==0.0.121
pip install transformers==4.28.1
pip install faiss-cpu==1.7.3
pip install streamlit==1.9.0
pip install python-dotenv==0.19.2
pip install sentence-transformers==2.2.2
pip install openai==0.27.0


## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/enigma-kun/rag-chatbot.git
    cd rag-chatbot
    ```

2. **Set up the environment:**
    Create a `.env` file in the project directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    streamlit run app.py
    ```

5. **Upload and process a PDF document:**
    - Use the sidebar to upload your PDF document and click "Process".
    - Once processed, you can start asking questions related to the document content.

## File Structure

- `app.py`: Main application script
- `htmlTemplates.py`: Contains HTML templates for the chat interface
- `requirements.txt`: List of required Python packages

## Usage

- **Upload PDF Document:** Use the file uploader in the sidebar to select and upload a PDF document.
- **Ask Questions:** Enter your question in the input box and press Enter. The chatbot will display the response based on the document content.

## Example

Here's an example of how to use the chatbot:

1. **Upload PDF:**
    - Upload the provided PDF document (e.g., `policy-booklet-0923.pdf`).

2. **Ask a Question:**
    - Enter a question like "What is the policy regarding accidents?" and press Enter.
    - The chatbot will retrieve the relevant information from the document and display the answer.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for providing the API
- [HuggingFace](https://huggingface.co/) for the embedding models
- [LangChain](https://langchain.com/) for the conversational retrieval chain framework
- [Streamlit](https://streamlit.io/) for the web application framework


[GitHub Repository Link](https://github.com/enigma-kun/rag-chatbot)
