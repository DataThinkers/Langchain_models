import os
import google.generativeai as geni
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

load_dotenv()

llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash")

st.title("Gemini Chat App")

prompt = st.text_input("Type your question and press enter")

if prompt:

    response = llm.invoke(prompt)

    st.write(response.content)