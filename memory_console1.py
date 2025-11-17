from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain.prompts import ChatPromptTemplate

load_dotenv()

chat_prompt = ChatPromptTemplate.from_messages(
       [("system","You are a friendly chatbot who answers questions politely."),
       ("human","{user_message}")])

llm = ChatOpenAI(model="gpt-4o-mini")

chain = chat_prompt | llm

while True:

    user_input = input("You:")

    if user_input.lower() in ["exit","quit","stop"]:
        print("Chat Ended")
        break

    response = chain.invoke({"user_message":user_input})

    print(response.content)

