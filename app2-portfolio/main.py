import streamlit as st

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