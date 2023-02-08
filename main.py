import streamlit as st
import pandas as pd

st.title("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna 
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(content)

st.header("Our Team")

col1,col2,col3 = st.columns(3)


df = pd.read_csv("data.csv",sep=",")
with col1:
    for index,row in df[:4].iterrows():
        first_name = row["first name"].title()
        last_name = row["last name"].title()
        st.subheader(f"{first_name} {last_name}")

        role = row["role"]
        st.write(role)

        image = "images/" + f"{row['image']}"
        st.image(image)

with col2:
    for index,row in df[4:8].iterrows():
        first_name = row["first name"].title()
        last_name = row["last name"].title()
        st.subheader(f"{first_name} {last_name}")

        role = row["role"]
        st.write(role)

        image = "images/" + f"{row['image']}"
        st.image(image)

with col3:
    for index,row in df[8:].iterrows():
        first_name = row["first name"].title()
        last_name = row["last name"].title()
        st.subheader(f"{first_name} {last_name}")
        role = row["role"]
        st.write(role)

        image = "images/" + f"{row['image']}"
        st.image(image)