import streamlit as st
import pandas
# Set webpage layout to wide
st.set_page_config(layout="wide")
# Add a header and some other text
st.title("The Best Company")
content = """
This is to test my skill on my website journey to
know what i can do and how i need to go further
from here because i need it in my journey
"""
st.write(content)
st.subheader("Our Team")
# Prepare the columns
# col1,col2,col3 = st.columns(3)
#col1, em1, col2, em2, col3 = st.columns([1.3,0.2,1.3,0.2,1.3])
col1, col2, col3 = st.columns(3)
# Make a dataframe with company members
df = pandas.read_csv("data.csv",sep=(","))
# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first name and last name
        st.header(row["first name"].title() + " " + row["last name"].title())
        # Add member's photo
        st.image("images/" + row["image"])
        # Add member's role in the company
        st.write(row["role"])
# Add content to the column
with col2:
    # Iterate over row 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first name and last names
        st.header(row["first name"].title() + " " + row["last name"].title())
        # Add member's photo
        st.image("images/" + row["image"])
        # Add member's role in the company
        st.write(row["role"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.image("images/" + row["image"])
        st.write(row["role"])