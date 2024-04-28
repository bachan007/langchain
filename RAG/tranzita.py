import os
import streamlit as st

from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama

from dotenv import load_dotenv
load_dotenv()


llm = Ollama(model='llama2')

prompt = ChatPromptTemplate.from_template(
"""
Provide me the accurate answers regarding the context.
<context>
{context}
<context>
Question:{input}
"""
)

document_chain = create_stuff_documents_chain(llm,prompt)

if 'vector' not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings()
    st.session_state.loader = WebBaseLoader('https://www.tranzita.com')
    st.session_state.docs = st.session_state.loader.load()
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
    st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)

retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever,document_chain)
prompt = st.text_input('Your Question ?')


st.title('Tranzita Systems Info')
if prompt:
    response = retrieval_chain.invoke({'input':prompt})
    print(response)
    st.write(response['answer'])
    