import streamlit as st
import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

load_dotenv()

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are an expert in the subject matter, you need to answer the queries.'),
        ('user','Question:{question}')
    ]
)

st.title('Langchain Integrated with ollama locally')
input_text = st.text_input("How can i assist You?")

# OLLAMA
llm = Ollama(model='llama2')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))