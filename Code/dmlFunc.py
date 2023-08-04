import streamlit as st
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="Movie_Booking_Tool",

)
cur = mydb.cursor()

def getMovieNames():
    cur.execute('SELECT Name FROM Movie ')
    data = cur.fetchall()
    return data

def getMovieDetails(movieName):
    cur.execute('SELECT Language,Genre,Target_Audience from Movie WHERE Name="{}"'.format(movieName))
    data = cur.fetchall()
    return data

def getTheaterNames():
    cur.execute('SELECT Name_of_Theatre FROM Theater ')
    data = cur.fetchall()
    return data

def getTheaterDetails(TheaterName1): 
    cur.execute('SELECT Name_of_Theatre,No_of_Screens,Area from Theatre WHERE Theatre.Theatre_ID="{}"'.format(TheaterName1))
    data = cur.fetchall()
    return data

def getTheaterMovie(selectMovie1):
    cur.execute('select Theatre_ID from Theatre JOIN Movie ON Movie_ID=M_ID WHERE Name="{}"'.format(selectMovie1))
    data1=cur.fetchall()
    return data1

def getshowid(selectTheater1):
    cur.execute('select Show_ID from Shows JOIN Theatre ON Theatre_ID=T_ID WHERE Theatre_ID="{}"'.format(selectTheater1))
    data=cur.fetchall()
    return data

def getShowDetails(selectshow1):
    cur.execute('SELECT Show_Time,Show_Date,Seats_Remaining_Gold,Seats_Remaining_Silver,Class_Cost_Gold,Class_Cost_Silver from Shows WHERE Show_ID="{}"'.format(selectshow1))
    data = cur.fetchall()
    return data

def cost(No_Tickets,selectshow,Select_Class):
    if Select_Class=="Gold Class":
        cur.execute('select Class_Cost_Gold from shows where Show_ID="{}"'.format(selectshow))
        data = cur.fetchall()
    else:
        cur.execute('select Class_Cost_Silver from shows where Show_ID="{}"'.format(selectshow))
        data = cur.fetchall()
    d=[i[0] for i in data]
    d1=d[0]
    data1=No_Tickets*d1
    
    return data1
