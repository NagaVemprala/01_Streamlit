import os
import streamlit as st
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

# Load environment variables
# load_dotenv() # Use this when running in local 

# Use the below option for cloud-based or web applications 
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def process_documents(uploaded_file):
    # Save uploaded file temporarily
    with open("temp.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load and process documents, specifying UTF-8 encoding
    loader = TextLoader("temp.txt", encoding="utf-8")  # Add encoding here
    documents = loader.load()

    # Split documents into chunks
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(documents)

    # Create embeddings and vector store
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(texts, embeddings)

    # Cleanup temporary file
    os.remove("temp.txt")

    return vector_store

def generate_answer(query, vector_store=None):
    llm = OpenAI(temperature=0)

    if vector_store:
        # Use document-based QA
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever()
        )
        answer = qa.invoke({"query": query})["result"]
    else:
        # Fallback to general knowledge
        answer = llm.invoke(query)

    return answer

# Streamlit UI
st.title("Document QA with OpenAI")

# File upload
uploaded_file = st.file_uploader("Upload a document", type=["txt"])

# Process documents only if file is uploaded
vector_store = None
if uploaded_file:
    vector_store = process_documents(uploaded_file)

# Query input
query = st.text_input("Enter your question:")

if query:
    # Generate and display answer
    answer = generate_answer(query, vector_store)
    st.subheader("Answer:")
    st.write(answer)