import streamlit as st
from send_email import send_email
import pandas as pd

df = pd.read_csv("app2-portfolio/challenge/topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    user_topic = st.selectbox("What topic do you want to discuss?",
                              (df["topic"]))
    message = st.text_area("Text")
    message = f"""\
    Subject: New email from {user_email}

    From: {user_email}
    {message}
    """

    button = st.form_submit_button("Submit")

    if button:
        try:
            send_email(message)
        except TimeoutError:
            print("The connection has been Timed out.")
        st.info("The email has been successfully sent!")

