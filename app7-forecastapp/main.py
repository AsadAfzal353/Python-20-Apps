import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecase Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                       ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures,
                        labels={"x": "Date",
                                "y": "Temperature (C)"})

        st.plotly_chart(figure)

    if option == "Sky":
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        lst = [f"app7-forecastapp/images/{condition.lower()}.png" for condition in sky_conditions]
        st.image(lst, width=115)