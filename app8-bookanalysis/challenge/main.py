import glob
import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("app8-bookanalysis/challenge/*.txt"))

analyzer = SentimentIntensityAnalyzer()

neg = []
pos = []

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()

    scores = analyzer.polarity_scores(content)
    pos.append(scores["pos"])
    neg.append(scores["neg"])

dates = [name.strip(".txt").strip("/app8-bookanalysis/challenge\\") for name in filepaths]

st.title("Diary Tone")

st.subheader("Positivity")
pos_figure = px.line(x=dates, y=pos,
                     labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=neg,
                     labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)

# run via: streamlit run app8-bookanalysis/challenge/main.py