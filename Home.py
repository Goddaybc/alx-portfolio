import streamlit as st
import pandas
# Set webpage layout to wide
st.set_page_config(layout="wide")
# Add a header and some other text
st.title("Tech-it")
content = """
Welcome to tech-it. This is the right sport for all
tech related services. Like it is said any problem that
can be solve with tech will be solve with tech. And that is what we
here at Tech-it
"""
st.write(content)
st.subheader("The Team")
# Prepare the columns
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