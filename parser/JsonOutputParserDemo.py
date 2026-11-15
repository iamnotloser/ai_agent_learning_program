from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from loguru import logger

load_dotenv(encoding="utf-8")

chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个{role}，请简短回答我提出的问题，结果返回json格式，q字段表示问题，a字段表示答案。",
        ),
        ("human", "请回答:{question}"),
    ]
)
prompt = chat_prompt.invoke(
    {"role": "AI助手", "question": "什么是LangChain，简洁回答100字以内"}
)

model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("QIANLIAN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

result = model.invoke(prompt)
logger.info(f"模型原始输出：{result}")

print("*" *60)

parser = JsonOutputParser()

response = parser.invoke(result)
logger.info(f"结构化输出结果：{response}")

print("*" *60)
print(response.get("a"))