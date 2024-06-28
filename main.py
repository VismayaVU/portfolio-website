import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Vismaya Vadana")
    content = """
    Hi, I am Vismaya Vadana. I am a budding undergraduate dedicated to gaining knowledge and skills to positively impact the world, striving to create meaningful change through innovative solutions and compassionate action.
    I currently study in PES University, Bengaluru (Ring Road campus) and I am in the process of completing my undergraduate degree in Computer Science Engineering (AI&ML).
    I enjoy coding in Python and love solving problems. I am also a huge sports enthusiast, especially in Football and Cricket.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
