from models.llm import llm

response = llm.invoke("What is LangGraph?")

print(response.content)