import streamlit as st
from dmlFunc import cost
from ddlFunc import Add_Booking

def bookingPage(Web_User_ID,selectMovie1,selectTheater1,selectshow):
   

    st.header("Book Your Ticket")
    
    col1, col2 = st.columns(2)
    with col1:
        Booking_ID = st.text_input("Booking ID:")
        Card_No = st.text_input("Enter your Card No.:")
        Name_on_card = st.text_input("Enter your name on card:")
        
    with col2:
        Select_Class = st.selectbox("Select ", ["Gold Class", "Silver Class"])
        No_Tickets = st.number_input("Ticket count:",0,100)
        Total_Cost = st.number_input("Bill:",cost(No_Tickets,selectshow,Select_Class))
    
       
    if st.button("Book"):
        #Add_Booking(Booking_ID ,No_Tickets, Total_Cost ,Card_No ,Name_on_card,selectshow,Web_User_ID)
        
        st.success("Successfully Booked Your Ticket")

