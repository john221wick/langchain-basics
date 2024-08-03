from langchain_community.llms import Ollama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda
from langchain.schema.output_parser import StrOutputParser


llm = Ollama(
    model="qwen2:0.5b"
)

messages = [
    ("system", "you are a good comedian"),
    ("human", "Tell me {x} jokes")
]

prompt = ChatPromptTemplate.from_messages(messages)

chain = prompt | llm

result = chain.invoke({"x": 3})

print(result)
