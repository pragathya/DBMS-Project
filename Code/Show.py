import streamlit as st
from dmlFunc import getshowid,getShowDetails
import pandas as pd
from Booking import bookingPage
import pandas as pd

def ShowPage(Web_User_ID,selectMovie1,selectTheater1):

    st.header("Select Your Show")

    showid =  [i[0] for i in getshowid(selectTheater1)]

    selectshow = st.radio("Select a Show", showid )
    selectedshow = getShowDetails(selectshow)
    

    if selectedshow:
        showtime=selectedshow[0][0]
        showdate=selectedshow[0][1]
        remgold = selectedshow[0][2]
        remsilver = selectedshow[0][3]
        goldcost = selectedshow[0][4]
        silvercost = selectedshow[0][5]

        col1, col2 = st.columns(2)
        with col1:
            b = st.metric("Date:", str(showdate))
            c = st.metric("Remaining Gold Seats :", remgold)
            e = st.metric("Cost of Gold Seat:", goldcost)
        with col2:
            a = st.metric("Show Time :",str(showtime))
            d = st.metric("Remaining Silver Seats :", remsilver)
            f = st.metric("Cost of silver Seat:", silvercost)
        

        # df = pd.DataFrame(selectedshow, columns=['Show Time','Date','Remaining Gold Seats' ,'Remaining Silver Seats ' ,'Cost of Gold Seat ','Cost of silver Seat'])
        # with st.expander("View Show Details"):
        #     st.table(df)

    
        bookingPage(Web_User_ID,selectMovie1,selectTheater1,selectshow)


    # df = pd.DataFrame(selectedshow, columns=['showtime','showdate','Remaining Gold Seats' ,'Remaining Silver Seats' ,'Cost of Gold Seat ','Cost of silver Seat'])
    # st.write(df.dtypes.astype(str))
    # with st.expander("View all Trains"):
    #     st.code(df)

       