import streamlit as st
import pandas as pd
from send_email import send_email


st.header("Contact Me")

df = pd.read_csv("topics.csv")
# lst = []

# for index,row in df.iterrows():
#     lst.append(row["topic"])
# new_tuple = tuple(lst)

with st.form(key="contact_me"):
    email_user = st.text_input("Your email address : ")
    option = st.selectbox("What topic do you want to discuss?",
                          df['topic'])
    user_message = st.text_area("Your message : ")
    submit = st.form_submit_button("Submit")
    if submit:
        send_email(email_user,option,user_message)
        st.info("Your email was sent successfully")

