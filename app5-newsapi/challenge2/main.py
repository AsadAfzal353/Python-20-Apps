import requests
import streamlit as st

st.set_page_config(layout="wide")

api_key= "oP7Ao9y1eHS6hyevyHaEon1qgAtM4i0WxxvkBqeJ"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)

content = request.json()

print(content)
st.header(content["title"])
st.image(content["url"])
st.write(content["explanation"])

