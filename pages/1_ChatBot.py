import streamlit as st
from src.retriever import retrieve_faq
from src.generator import generate_answer

st.title("FAQ chatbot")
user_question = st.chat_input("Your message")
if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_question:
    with st.chat_message("user"):
        st.write(user_question)
   
    st.session_state.history.append({"role": "user", "content": user_question})
    result = retrieve_faq(user_question)
    answer = generate_answer(user_question, result["documents"][0], result["distances"][0])
    with st.chat_message("assistant"):
        st.write(answer)
    st.session_state.history.append({"role": "assistant", "content": answer})
