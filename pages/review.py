import streamlit as st
from nav import switch_page

if st.button("⬅️ Go Back"):
    switch_page("main")
    
st.title("Review")
st.divider()



