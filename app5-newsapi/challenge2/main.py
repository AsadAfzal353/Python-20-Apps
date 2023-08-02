import requests
import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.title = "NASA1"

with col2:
    st.title = "NASA2"


# api_key= "oP7Ao9y1eHS6hyevyHaEon1qgAtM4i0WxxvkBqeJ"
# url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# request = requests.get(url)

# content = request.json()

# print(content)
# st.header = content["title"]
# st.image = content["hdurl"]
# st.write = content["explanation"]

st.info = "NASA"
