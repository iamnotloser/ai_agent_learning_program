import os
from dotenv import load_dotenv
from langchain.chat_models import (
    init_chat_model,
)
from openai import api_key

load_dotenv(encoding="utf-8")

deep_llm = init_chat_model(
    model = "",
    model_provider="openai",
    api_key=os.getenv("DEEP_API_KEY")
)