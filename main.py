import streamlit as st
import os
from nav import switch_page
from src.models import generate, tasks

st.title("Insight AI")

st.markdown("This is a place where you can save your thoughts, ideas, inspiration, and more.")

text = st.text_area("test",key="text",label_visibility="hidden")

st.write(f'You wrote {len(text)} characters.')

if st.button("Save", use_container_width=True, type="primary"):
    # Check if txt length is greater than 20 characters
    if len(text) > 50:
        st.divider()
        col1, col2 = st.columns([6,4])
        with col1:
            st.header("🪄 Today in Brief: ")
            st.markdown(generate(text))
        with col2:
            st.header("✅ Actions: ")
            st.markdown(tasks(text))
    else:
        st.info("Please enter more than 20 characters before summarizing.")
