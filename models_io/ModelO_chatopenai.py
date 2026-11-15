from langchain_openai import ChatOpenAI
import os

from dotenv import load_dotenv

from openai import base_url

load_dotenv(encoding="utf-8")

chat_llm = ChatOpenAI(
    model = "qwen3.8-flash",
    api_key = os.getenv("QIANLIAN_API_KEY"),
    base_url = os.getenv("QIANLIAN_BASE_URL"),
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁？"},
]
response = chat_llm.invoke(messages)
print(response.content)