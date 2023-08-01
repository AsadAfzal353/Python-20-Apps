import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("app2-portfolio/images/asad.jpg")

with col2:
    st.title("Asad Afzal")
    content = """
    Hello everyone, my name is Asad Afzal and currenlty I am learning python which would be
    fundamentals for my journey of being an Artificial Intelligence Engineer.
    """
    st.info(content)

content2 = """
    Below you can find ome of the apps I have built in Python. Feel free to contact me!
    """
st.write(content2)

col3, empty_col, col4 = st.columns([3, 1, 3])
df = pd.read_csv("app2-portfolio/data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("app2-portfolio/images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("app2-portfolio/images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")