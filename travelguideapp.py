from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain.prompts import ChatPromptTemplate
import streamlit as st

load_dotenv()

st.title("Travel Guide App")

tone = st.selectbox("Choose Tone:",["Friendly","Formal","Funny"])

city = st.text_input("Enter a City name","Anand")

chat_prompt = ChatPromptTemplate.from_messages(
       [("system","You are a {tone} travel guide who provides interesting facts about cities."),
       ("human","Tell me 3 unique facts about {city}")])

values = {
        "tone":tone ,
        "city" :city,
    
}

if st.button("Find Facts"):
    message = chat_prompt.invoke(values)

    llm = ChatOpenAI(model="gpt-4o-mini")

    response = llm.invoke(message)

    st.subheader(f"Travel Facts about {city}")

    st.write(response.content)

