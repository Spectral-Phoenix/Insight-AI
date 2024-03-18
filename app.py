import time
import streamlit as st

from src.scrape import scrape
from src.search import quick_web_search, deep_web_search
from src.summarise import summarise

st.markdown("<h1 style='text-align: center;'>Insight AI - DTI Project</h1>", unsafe_allow_html=True)

# Using Streamlit's columns to layout input and button side by side
col1, col2 = st.columns([3, 1])  # Adjust the ratio as needed



user_query = st.text_input("Enter the Query: ", label_visibility="hidden", key='user_query')

if st.button("Search", key='search_button', help="Click to start search"):
    start_time = time.time()
    # Search the Web and Collect Links
    links = quick_web_search(user_query)
    st.info("Web Search Completed!")
    # Scrape the Text from the Links
    text = scrape(links)
    answer = summarise(user_query, text)
    end_time = time.time()
    elapsed_time = "{:.2f}".format(end_time - start_time)
    st.markdown(f"\nAnswer:\n {answer}")
    st.text(f"Time Elapsed: {elapsed_time} seconds")