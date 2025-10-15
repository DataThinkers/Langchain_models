import os

import streamlit as st
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3.2:3b")

st.title("Ollama Chat App")

prompt = st.text_input("Type your question and Press Enter:")

if prompt:
    response = llm.invoke(prompt)

    st.write(response.content)