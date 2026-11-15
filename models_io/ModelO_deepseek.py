import os
from langchain_deepseek import ChatDeepSeek

from dotenv import load_dotenv

load_dotenv(encoding="utf-8")

model = ChatDeepSeek(
    model="deepseek-v4-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)
print(model.invoke("什么是 LangChain？100 字以内回答，简洁。").content)