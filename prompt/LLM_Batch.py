import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QIANLIAN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

questions = [
    SystemMessage(content="你是一个法律助手，只回答法律问题，超出范围的统一回答，非法律问题无可奉告"),
    HumanMessage(content="简单介绍下广告法，一句话告知50字以内"),
]
response = model.stream(questions)
print(f"相应类型：{type(response)}")

for chunk in response:
    print(chunk.content,end="",flush=True)
print("\n")

