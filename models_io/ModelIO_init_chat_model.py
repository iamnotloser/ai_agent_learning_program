import os
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
from openai import base_url

load_dotenv(encoding="utf-8")

model = init_chat_model(
    model = "kimi-k3.1-pro",
    api_key = os.getenv("KIMI_API_KEY"),
    base_url = "https://api.moonshot.cn/v1",
    model_provider= "openai",

)
print(model.invoke("写一句关于春天的词，14 字以内"))
print(type(model))
# <class 'str'>
print(type(model.invoke("写一句关于春天的词，14 字以内").content))
# <class 'langchain_core.messages.ai.AIMessage'>
print(type(model.invoke("写一句关于春天的词，14 字以内")))