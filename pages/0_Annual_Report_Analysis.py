import os
import streamlit as st
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Set the OpenAI API key
# os.environ["OPENAI_API_KEY"] = 'ENTER YOUR API KEY'

# Streamlit app
st.title("Annual Report Analysis")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file to analyse:", type="pdf")
user_input = st.text_input("Enter a query")

if uploaded_file is not None and user_input:
    # Process the PDF
    loader = PyMuPDFLoader(uploaded_file)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    persist_directory = "./storage"
    vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=persist_directory)
    vectordb.persist()

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    llm = ChatOpenAI(model_name='gpt-4')
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    if st.button("Chat"):
        query = f"###Prompt {user_input}"
        try:
            llm_response = qa(query)
            st.write(llm_response["result"])
        except Exception as err:
            st.error(f'Exception occurred: {str(err)}')
