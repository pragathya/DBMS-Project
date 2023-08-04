import streamlit as st
from ddlFunc import Add_Theater
from dmlFunc import getTheaterNames,getTheaterDetails,getTheaterMovie
from Show import ShowPage

def TheaterPage(Web_User_ID,selectMovie1):

    st.header("Check for theatres")

    Theatersid =  [i[0] for i in getTheaterMovie(selectMovie1)]

    selectTheater = st.radio("Select a Theatre", Theatersid )
    selectedTheater = getTheaterDetails(selectTheater)

    print("selectTheater",selectTheater)
    print("selectedTheater",selectedTheater)
    
    if selectedTheater:
        tname=selectedTheater[0][0]
        noscreens = selectedTheater[0][1]
        are = selectedTheater[0][2]
    
    
        ar = st.text_input("Theater Name :", tname)
        ns = st.text_input("No of screens Available:", noscreens)
        ar = st.text_input("Location :", are)

        # if st.button("Proceed With This Theater"):
        #     add_data(selectTheater)
        ShowPage(Web_User_ID,selectMovie1,selectTheater)
            

        

    