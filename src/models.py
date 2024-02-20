from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

gemini_api = st.secrets["api_key"]

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",temperature=0.5, google_api_key=gemini_api
)

def generate(text):

    prompt1 = '''from the journal entry, identify important events that happened today, 
                            donot include uncompleted tasks or events'''

    message = prompt1 + text
    summary = llm.invoke(message)

    return summary.content

def tasks(text):
    prompt2 = '''From the journal entry Provided, identify the incomplete tasks or actions 
                            that need to be completed and return them, if there are no tasks, then return a message saying no tasks'''
    message = prompt2 + text
    summary = llm.invoke(message)

    return summary.content