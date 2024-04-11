import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn

load_dotenv()

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

llm = Ollama(model='llama2')

app = FastAPI(
    title="LangServe"
)

add_routes(
    app,
    ChatOpenAI(),
    path='/llama2'
)

prompt = ChatPromptTemplate.from_template('tell me a joke on {joke}')

add_routes(
    app,
    prompt|llm,
    path="/joke"
)

if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)