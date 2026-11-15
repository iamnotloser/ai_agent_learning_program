from langchain_core.prompts import  PromptTemplate

template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}"
)

partial = template.partial(role="python开发")
print(partial)
print(type(partial))
print()

# ---------- 3. 对新模板 format，只传 question 即可 ----------
prompt = partial.format(question="冒泡排序怎么写？")
print(prompt)
print(type(prompt))
