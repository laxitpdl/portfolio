import streamlit as st

st.header("Contact us")

with st.form(key = "email_forms" ):
    user_email= st.text_input("Your mail...")
    message = st.text_area("Your message...")

    button = st.form_submit_button()