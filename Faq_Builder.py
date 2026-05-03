import streamlit as st
from src.database import add_faq, reset_collection, get_all

st.set_page_config(page_title="FAQ Builder")

st.title("Add the FAQ module:")
st.text("Add a relevant FAQ to train the chatbot")
question = st.text_input("Add your FAQ Question")
answer = st.text_input("Add your FAQ Answer")

if st.button("Add the FAQ"):
    if question and answer:
        add_faq(question,answer)
        st.success("FAQ added succesfully, you can try it out on the chatbot app or you can add more FAQs")
    else:
        st.error("Add question or answer")
        

if st.button("Reset all FAQ"):
    reset_collection()

if st.button("Show all the FAQ"):
    all_faqs = get_all()
    for faq in all_faqs:
        st.text(faq)