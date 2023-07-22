import streamlit as st
import bcrypt


def register_user(username, password):
    # Generate a salt and  hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Store the username and hashed password in database or file
    # Here, i am using a simple text file
    with open('user.txt', 'a') as file:
        file.write(f"{username}:{hashed_password.decode()}\n")


def login_user(username, password):
    with open("user.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if stored_username == username:
                # Check if the provided passowrd matches the  hashed password
                if bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8")):
                    return True
    return False


def main():
    st.title("User Authentication")

    # Sidebar for user  registration
    st.sidebar.title("Register:violet")
    new_username = st.sidebar.text_input("Username")
    new_password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Register"):
        register_user(new_username, new_password)
        st.sidebar.success("Registration successful!")
    # Main content for the user login
    st.header("Login")
    username = st.text_input("Username", key="username")
    password = st.text_input("Password", key="password")
    if st.button("Login"):
        if login_user(username, password):
            st.success("Login successful")
        else:
            st.error("Invalid username or password")


if __name__ == "__main__":
    main()
