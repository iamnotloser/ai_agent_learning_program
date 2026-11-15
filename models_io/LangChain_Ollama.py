from langchain_ollama import ChatOllama

model = ChatOllama(
    base_url = "http://localhost:11434",
    model = "nemotron-3.5-bolt:e4b",
    reasioning = False,
)

response = model .invoke("什么是LangChain,100字以内回答")
print(response)
print(response.content
      )