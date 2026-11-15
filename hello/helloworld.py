import os
from dotenv import load_dotenv
from langchain.chat_models import (
    init_chat_model,
)
from openai import api_key

load_dotenv(encoding="utf-8")

deep_llm = init_chat_model(
    model = "kimi-k3",
    model_provider="openai",
    api_key=os.getenv("KIMI_API_KEY"),
    base_url="https://api.moonshot.cn/v1"

)

print(deep_llm.invoke("你是谁").content)