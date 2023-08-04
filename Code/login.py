import streamlit as st
from ddlFunc import Add_User
from movies import MoviesPage

def loginPage():
    
    col1, col2 = st.columns(2)
    with col1:
        Web_User_ID = st.text_input("User ID:")
        First_Name = st.text_input("First Name:")
        Last_Name = st.text_input("Last Name:")
    with col2:
        Email_ID = st.text_input("Email ID:")
        Age = st.text_input("Age:")
        Phone_Number = st.text_input("Phone No:")

    if st.button("Sign in"):
        Add_User(Web_User_ID ,First_Name, Last_Name ,Email_ID ,Age ,Phone_Number)
        st.success("Successfully logged in: {}".format(First_Name))
    
    


    MoviesPage(Web_User_ID)
        

