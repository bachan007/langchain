import requests
import streamlit as st

def capture_response(text_input):
    response = requests.post("http://localhost:8000/joke/invoke",
                             json={'input':{'joke':text_input}})
    print(response.json())
    return response.json()['output']

st.title('Langchain calling API')
input_text = st.text_input("How can i assist You?")

if input_text:
    st.write(capture_response(input_text))