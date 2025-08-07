import streamlit as st

st.set_page_config(page_title="AI Profit Suite", layout="wide")

st.title("Welcome to AI Profit Suite Pro™")
st.markdown("### Community. Collaboration. Unity.")
st.write("Use the left sidebar to begin creating content, scheduling automation, or viewing your performance.")

# Example buttons to start
if st.button("Generate Affiliate Post"):
    st.success("AI is now generating your affiliate content...")

if st.button("Schedule Social Media Post"):
    st.info("Scheduling your post now...")

st.sidebar.header("Navigation")
st.sidebar.markdown("Select a task from the sidebar to begin.")
