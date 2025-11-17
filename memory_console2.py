from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain.prompts import ChatPromptTemplate

from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

load_dotenv()

chat_prompt = ChatPromptTemplate.from_messages(
       [("system","You are a friendly chatbot who answers questions politely."),
        MessagesPlaceholder(variable_name="history"),
       ("human","{user_message}")])

history = ChatMessageHistory()

llm = ChatOpenAI(model="gpt-4o-mini")

chain = chat_prompt | llm

runnable = RunnableWithMessageHistory(
    chain,
    get_session_history=lambda _ : history,
    history_messages_key="history",
    input_messages_key="user_message"
)

while True:

    user_input = input("You:")

    if user_input.lower() in ["exit","quit","stop"]:
        print("Chat Ended")
        break

    response = runnable.invoke({"user_message":user_input},
                               config={"configurable":{"session_id":"demo"}})

    print(response.content)
    # Just one simple print of history
    # print(history.messages)
    #print([m.content for m in history.messages])

