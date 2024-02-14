import streamlit as st
import os
from nav import switch_page
from langchain_google_genai import ChatGoogleGenerativeAI

api_gemini = st.secrets["api_key"]

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",temperature=0.5, google_api_key=api_gemini
)

st.title("Insight AI")

st.markdown("This is a place where you can save your thoughts, ideas, inspiration, and more.")

text = st.text_area("",key="text")

st.write(f'You wrote {len(text)} characters.')

if st.button("Save", use_container_width=True, type="primary"):
    # Check if txt length is greater than 20 characters
    if len(text) > 50:
        st.divider()
        col1, col2 = st.columns([6,4])
        with col1:
            st.header("🪄 Today in Brief: ")
            # Create prompt and message with txt
            prompt1 = '''from the journal entry, identify important events that happened today, 
                        donot include uncompleted tasks or events'''
            message = prompt1 + text
            summary = llm.invoke(message)
            st.markdown(summary.content)
        with col2:
            st.header("✅ Actions: ")
            prompt2 = '''From the journal entry Provided, identify the incomplete tasks or actions 
                        that need to be completed and return them, if there are no tasks, then return a message saying no tasks'''
            message = prompt2 + text
            summary = llm.invoke(message)
            st.markdown(summary.content)
    else:
        st.info("Please enter more than 20 characters before summarizing.")
