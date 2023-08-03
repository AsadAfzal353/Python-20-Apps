import streamlit as st
import plotly.express as px
import pandas as pd


st.title("In Search of Happiness")

df = pd.read_csv("app7-forecastapp/challenge/happy.csv")


option_x = st.selectbox("Select the data for the X-axis",
                        (df.columns))
option_y = st.selectbox("Select the data for the Y-axis",
                        (df.columns))

st.subheader(f"{option_x.title()} and {option_y.title()}")

figure1 = px.scatter(x=df[option_x], y=df[option_y],
                     labels={"x":option_x.title(),
                            "y":option_y.title()})

st.plotly_chart(figure1)
