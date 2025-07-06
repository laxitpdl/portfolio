import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

#  HEADER SECTION 
col1, col2 = st.columns(2)

with col1:
    st.image("images/npl.png")  # Reduced size for better layout

with col2:
    st.title("Lakshit Poudel")
    st.write(
        "Hi! I’m Lakshit Poudel, an aspiring programmer from Nepal, now based in the U.S. "
        "I build real-world apps using Python, AI, and Streamlit. Self-taught and hyper-focused, "
        "I blend code with logic to solve meaningful problems and push my limits — in tech and in life."
    )

# APP SECTION INTRO 
st.info("Below you can see my apps — feel free to try them and share your experience!")

#  LOAD PROJECT DATA 
df = pd.read_csv("data.csv", sep=';')

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

#  LEFT COLUMN PROJECTS 
with col3:
    for index, row in df[:10].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.markdown(f"[Source Code]({row['url']})")

#  RIGHT COLUMN PROJECTS 
with col4:
    for index, row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.markdown(f"[Source Code]({row['url']})")
