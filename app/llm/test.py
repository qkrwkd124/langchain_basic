from google import genai
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import getpass
import os

load_dotenv()

client = genai.Client()
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "너는 친절한 한국어 AI 어시스턴트야."),
        ("user", "{question}"),
    ]
)

chain = prompt | model | StrOutputParser()

response = chain.invoke({"question": "이거 모델은 뭐야"})
print(response)