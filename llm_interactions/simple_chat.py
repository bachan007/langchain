from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os


prompt1 = ChatPromptTemplate.from_messages(
    [
        ('system','''You are a talkative person, who has inquisitiveness, who have too many questions.
        So, You need to start by asking a question, one question at a time only. It can be anything.
        Example: 
        Que1. Why the colour of the sky is Blue?
        Que2. Why the Colour of the ocean is Blue?
        Que3. How monkeys can jump so long?
        Que4. Why the wind flows?
        Etcetra Etcetra Etcetra.....'''),
        ('user','Question:{question}')    
                ]
)

llm1 = Ollama(model='llama2')
outputParser1 = StrOutputParser()
chain1 = prompt1|llm1|outputParser1

prompt2 = ChatPromptTemplate.from_messages(
    [
        ('system','''You are a person having answer of all the questions
         You are a very smart person, who can give the answer in the layman as well as in expert mode.
         So you need to provide the answer in the very beautiful manner so that
         anyone can get what you are trying to explain.'''),
         ('user','Question:{question}')    
                 ]
)

llm2 = Ollama(model='llama2')
outputParser2 = StrOutputParser()
chain2 = prompt2|llm2|outputParser2


def question():
    question = chain1.invoke({'question':'''Ask me a Question which is not provided to you in the example.
                        You do not need to provide the answer of that question. 
                        You can not ask more than one question.
                        User perfix "Que." before starting the exact question
                        '''})

    que = question.split('Que')[1][3:]
    return que

def answer(question):
    answer = chain2.invoke({'question':question})
    return answer

st.title('Local llms interaction.')
input_text = st.text_input("How many question answers you need?")

if input_text:
    count = 1
    while count<=int(input_text):
        st.write(f"Question{count}.\n")
        st.write('As it is running on local machine, So taking time to ask the Question....')
        ques = question()
        st.write(ques)
        st.write('Please be patient, You will get the answer.........')
        st.write('Answer:\n')
        ans = answer(ques)
        st.write(ans)
        st.write('*****************')
        count+=1
# # as of now i am taking the count as 5
# count = 1
# while count<=2:
#     print(f"Question{count}.\n")
#     print('As it is running on local machine, So taking time to ask the Question....')
#     ques = question()
#     print(ques)
#     print('Please be patient, You will get the answer.........')
#     print('Answer:\n')
#     ans = answer(ques)
#     print(ans)
#     print('*****************')
#     count+=1

