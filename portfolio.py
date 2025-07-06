#https://laxitpdl-my-todo-webapp-web-axotkz.streamlit.app/

import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1: 
    st.image("images/npl.png")

with col2:
    st.title("Lakshit Poudel")
    comment = """ Hi! I’m Lakshit Poudel, an aspiring programmer originally from Nepal. Currently based in the U.S. I am a Self-taught and hyper-focused, I blend engineering logic with AI tools to build real-world apps — from Python automation to Streamlit web apps, from machine learning models to full-stack dev.
Fluent in both code and calculation, I aim to solve meaningful problems and push my limits — whether in tech or in life."""
    st.write(comment)
              

comment2 = """ Below you can see my apps and fell free to share your experience!!"""

st.info(comment2) 


col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])