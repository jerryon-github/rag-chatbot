import streamlit as st
from src.api import get_answer

st.title("💬 RAG Chatbot with Context Memory")
query = st.text_input("Ask a question about your documents:")

if query:
    response = get_answer(query)
    st.write("**Answer:**", response)
