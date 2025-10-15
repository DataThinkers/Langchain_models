import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

import streamlit as st

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

st.title("OpenAI Chat App")

prompt = st.text_input("Type your question and Press Enter:")

if prompt:
    response = llm.invoke(prompt)

    st.write(response.content)