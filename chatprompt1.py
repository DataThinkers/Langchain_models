from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain.prompts import ChatPromptTemplate

load_dotenv()


chat_prompt = ChatPromptTemplate.from_messages(
       [("system","You are a strict computer science teacher"),
       ("human","explain {topic} in simple language.")])


message = chat_prompt.invoke({"topic":"Neural Networks"})

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke(message)

print(response.content)

