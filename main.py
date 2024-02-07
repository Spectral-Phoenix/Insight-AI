import streamlit as st

st.title("Insight AI")

st.markdown("This is a place where you can save your thoughts, ideas, inspiration, and more.")

txt = st.text_area(
    "Jot down your thoughts",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
    )

st.write(f'You wrote {len(txt)} characters.')

if st.button("Save",use_container_width=True, type="primary"):
    st.balloons()
    st.success("Your thoughts have been saved!")