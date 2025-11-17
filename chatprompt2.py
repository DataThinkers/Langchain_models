from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain.prompts import ChatPromptTemplate

load_dotenv()


chat_prompt = ChatPromptTemplate.from_messages(
       [("system","You are a {tone} {subject} teacher."),
       ("human","explain {topic} to a {audience} in simple language.")])

values = {
        "tone": "Funny",
        "subject" : "Computer Science",
        "topic" : "Data Structures",
        "audience" : "beginners"

}

message = chat_prompt.invoke(values)

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke(message)

print(response.content)

