from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

gemini_api = st.secrets["api_key"]

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",temperature=0.5, google_api_key=gemini_api
)

def generate(text):

    prompt = " "

    message = prompt1 + text
    summary = llm.invoke(message)

    return summary.content