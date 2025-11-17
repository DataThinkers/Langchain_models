import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.prompts import PromptTemplate

import streamlit as st

load_dotenv()

st.title("City Fact Finder App")

city = st.text_input("Enter a city")
topic = st.text_input("Enter a Topic (e.g food, history, culture, architecture..)")
language = st.text_input("Enter a language")

template = """
    you are a travel expert.
    Avoid giving information about fictional or non-existent cities.
    If the city is fictional or does not exist, answer exactly: I don't know.
    Share one interesting or fun fact about {topic} in {city}.
    answer in {language}

"""

prompt = PromptTemplate(
    input_variables=["topic","city","language"],
    template=template

)
final_prompt = prompt.format(topic=topic, city=city,language=language)

if st.button("Generate"):
    llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash",temperature=0.7)
    response = llm.invoke(final_prompt)
    st.write(response.content)