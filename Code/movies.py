import streamlit as st
from ddlFunc import Add_Movies,Add_Theater
from dmlFunc import getMovieNames,getMovieDetails
from Theater import TheaterPage


def MoviesPage(Web_User_ID):

    st.subheader("Select A Movie")
    
    movies =  [i[0] for i in getMovieNames()]

    selectMovie = st.selectbox("Select a Movie", movies) 
    selectedMovie = getMovieDetails(selectMovie)

    # print("selectMovie",selectMovie)
    # print("selectedMovie",selectedMovie)
    # st.write(selected_result)
    if selectMovie:
        lang = selectedMovie[0][0]
        genre = selectedMovie[0][1]
        taudi = selectedMovie[0][2]
    

        l = st.text_input("Language:", lang)
        g = st.text_input("Genre:", genre)
        t = st.text_input("Target Audience:", taudi)


        TheaterPage(Web_User_ID,selectMovie)
        
        


    
       

   
   

