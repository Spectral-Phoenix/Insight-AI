import streamlit as st

#from dotenv import load_dotenv
from langchain_community.llms import Cohere
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

#load_dotenv()

api_key = st.secrets["GEMINI_API_KEY"]
api_key_1 = st.secrets["COHERE_API_KEY"]
api_key_2 = st.secrets["GROQ_API_KEY"]

llm = ChatGoogleGenerativeAI(model="gemini-pro",
                                google_api_key=api_key,
                                temperature = 0.5)

llm1 = Cohere(model="command-nightly",
                cohere_api_key = api_key_1,
                max_tokens=4096,
                temperature=0.5,)

llm2 = ChatGroq(temperature=0.5,
                groq_api_key=api_key_2, 
                model_name="mixtral-8x7b-32768")