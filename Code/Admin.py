import pandas as pd
import streamlit as st
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="Movie_Booking_Tool",

)
c= mydb.cursor()

def view_all_data():
    c.execute('SELECT * FROM movie')
    data = c.fetchall()
    return data

def view():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Movie_ID','Name','Language' ,'Genre' ,'Target_Audience '])
    with st.expander("View all Movies"):
        st.dataframe(df)

def add_data(ID, Name, lang, Genre, ta):
    c.execute('INSERT INTO movie VALUES (%s,%s,%s,%s,%s);',
              (ID, Name, lang, Genre, ta))
    mydb.commit()
def create():
    col1, col2 = st.columns(2)
    with col1:
        ID = st.text_input("Movie ID:")
        Name = st.text_input("Name:")
        lang = st.text_input("Language:")
    with col2:
        Genre = st.text_input("Genre: ")
        ta = st.text_input("Target Audience")

    if st.button("Add Movie"):
        add_data(ID, Name, lang, Genre, ta)
        st.success("Successfully added Movie: {}".format(Name))



def view_only_movie_names():
    c.execute('SELECT Name FROM Movie')
    data = c.fetchall()
    return data
def get_details(movie_name):
    c.execute('SELECT * FROM Movie WHERE Name="{}"'.format(movie_name))
    data = c.fetchall()
    return data   
def edit_details(new_Mid, new_Mname, new_lang, new_genre, new_mte, Mid, Mname, Mlang,Mgnere, Mta):
    c.execute("UPDATE Movie SET Movie_ID=%s, Name=%s, Language=%s, Genre=%s, Target_Audience=%s WHERE "
              "Movie_ID=%s and Name=%s and Language=%s and Genre=%s and Target_Audience=%s ", (new_Mid, new_Mname, new_lang, new_genre, new_mte, Mid, Mname, Mlang,Mgnere, Mta))
    mydb.commit()



def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Movie_ID','Name','Language' ,'Genre' ,'Target_Audience '])
    with st.expander("Current Movies"):
        st.dataframe(df)
    list_of_movies = [i[0] for i in view_only_movie_names()]
    selected_train = st.selectbox("Movie to Edit", list_of_movies)
    selected_result = get_details(selected_train)
    # st.write(selected_result)
    if selected_result:
        Mid = selected_result[0][0]
        Mname = selected_result[0][1]
        Mlang = selected_result[0][2]
        Mgnere = selected_result[0][3]
        Mta = selected_result[0][4]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_Mid = st.text_input("Movie ID:", Mid)
            new_Mname = st.text_input("Name:", Mname)
        with col2:
            new_lang = st.text_input("Language:",Mlang)
            new_genre = st.text_input("Genre:",Mgnere)
            new_mta = st.text_input("Target Audience",Mta)

        if st.button("Update Movie"):
            edit_details(new_Mid, new_Mname, new_lang, new_genre, new_mta, Mid, Mname, Mlang,Mgnere, Mta)
            st.success("Successfully updated:: {} to ::{}".format(Mname, new_Mname))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Movie_ID','Name','Language' ,'Genre' ,'Target_Audience '])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_data(selected_movie):
    c.execute('DELETE FROM Movie WHERE Name="{}"'.format(selected_movie))
    mydb.commit()
def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Movie_ID','Name','Language' ,'Genre' ,'Target_Audience '])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_movies = [i[0] for i in view_only_movie_names()]
    selected_movie = st.selectbox("Movie to Delete", list_of_movies)
    st.warning("Do you want to delete ::{}".format(selected_movie))
    if st.button("Delete Movie"):
        delete_data(selected_movie)
        st.success("Movie has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Movie_ID','Name','Language' ,'Genre' ,'Target_Audience '])
    with st.expander("Updated data"):
        st.dataframe(df2)