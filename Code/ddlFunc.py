import streamlit as st
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="Movie_Booking_Tool",

)
cur = mydb.cursor()


def UserTable():
    cur.execute("CREATE TABLE IF NOT EXISTS Web_user(Web_User_ID varchar(5),First_Name varchar(15), Last_Name varchar(20),Email_ID varchar(30),Age int,Phone_Number varchar(10) NOT NULL, Primary Key(Web_User_ID));")


def Add_User(Web_User_ID ,First_Name, Last_Name ,Email_ID ,Age ,Phone_Number):
    cur.execute('INSERT INTO Web_user (Web_User_ID ,First_Name, Last_Name ,Email_ID ,Age ,Phone_Number) VALUES (%s,%s,%s,%s,%s,%s);',
              (Web_User_ID ,First_Name, Last_Name ,Email_ID ,Age ,Phone_Number))
    mydb.commit()

def MoviesTable():
    cur.execute("Create Table IF NOT EXISTS Movie(Movie_ID varchar(5),Name varchar(30) NOT NULL,Language varchar(10),Genre varchar(20),Target_Audience varchar(5),Primary Key(Movie_ID));")

def Add_Movies():
    cur.execute("Insert into Movie values('001', 'Hichki', 'Hindi','Drama/Comedy', 'U/A'),('002', 'Pacific Rim Uprising',  'English','Fantasy/SciFi', 'U/A'),('003', 'Strangers : Prey at night','English', 'Horror', 'U/A'),('004', 'Tomb Raider', 'English','Fantasy/Action', 'A'),('005', 'Black Panther','English', 'Fantasy/SciFi','U/A');")
    mydb.commit()

def TheaterTable():
    cur.execute("CREATE TABLE IF NOT EXISTS Theatre(Theatre_ID varchar(5),Name_of_Theatre varchar(30) NOT NULL, No_of_Screens int,Area varchar(30),M_ID varchar(10), Foreign Key (M_ID) REFERENCES Movie (Movie_ID) ON DELETE CASCADE ON UPDATE CASCADE, Primary Key(Theatre_ID));")

def Add_Theater():
    cur.execute("Insert into Theater values('T01', 'PVR Cinemas', 4, 'Koramangala, Bangalore','001'),('T02', 'INOX Movies', 4, 'Katpadi, Vellore','002'),('T03', 'Ciinepolis', 3, 'Meera Nagar, Gurgaon','003'),('T04', 'INOX Movies', 4, 'Rajainagar, Bangalore','001'),('T05', 'INOX Movies', 2, 'Rajainagar, Bangalore','002'),('T06', 'Cinepolis', 3, 'Whitefield, Bangalore','003'),('T07','Cinepolis',1,'Whitefield,Bangalore','004'),('T08', 'PVR Cinemas', 1, 'Indra Nagar, Bangalore','005');")
    mydb.commit()



# def ScreenTable():
#     cur.execute("CREATE TABLE IF NOT EXISTS Screen(Screen_ID varchar(5),No_of_Seats_Gold int NOT NULL,No_of_Seats_Silver int NOT NULL,Theatre_ID varchar(5),Primary Key(Screen_ID),Foreign Key(Theatre_ID) REFERENCES Theater(Theatre_ID) ON DELETE CASCADE ON UPDATE CASCADE);")

# def Add_Screen():
#     cur.execute("Insert into Screen values ('S0101', 20, 60, 'T01'), ('S0102', 10, 30, 'T01'), ('S0103', 5, 10, 'T01'), ('S0104', 20, 40, 'T01'), ('S0201', 22, 64, 'T02'), ('S0202', 5, 7, 'T02'), ('S0203', 15, 30, 'T02'), ('S0204', 17, 40, 'T02'), ('S0301', 20, 50, 'T03'), ('S0302', 30, 60, 'T03'), ('S0303', 15, 20, 'T03'),('S0401', 16, 44, 'T04'),('S0402', 12, 32, 'T04'),('S0501', 2, 8, 'T05'),('S0601', 14, 28, 'T06'),('S0602', 32, 40, 'T06'),('S0701', 8, 16, 'T07'),('S0801', 4, 8, 'T08');")
#     mydb.commit()

def ShowTable():
    cur.execute("CREATE TABLE IF NOT EXISTS Shows(Show_ID varchar(10),Show_Time varchar(10) NOT NULL,Show_Date varchar(15) NOT NULL,Seats_Remaining_Gold int NOT NULL CHECK (Seats_Remaining_Gold >= 0),Seats_Remaining_Silver int NOT NULL CHECK (Seats_Remaining_Silver >= 0),Class_Cost_Gold int NOT NULL,Class_Cost_Silver int NOT NULL,T_ID varchar(5) NOT NULL,Movie_ID varchar(5) NOT NULL,Primary Key(Show_ID),Foreign Key (T_ID) REFERENCES Theater(Theatre_ID) ON DELETE CASCADE ON UPDATE CASCADE,Foreign Key (Movie_ID) REFERENCES Movie(Movie_ID) ON DELETE CASCADE ON UPDATE CASCADE);")
    #cur.execute("CREATE TABLE IF NOT EXISTS Shows(Show_ID varchar(10),Show_Time time NOT NULL,Show_Date date NOT NULL,Seats_Remaining_Gold int NOT NULL CHECK (Seats_Remaining_Gold >= 0),Seats_Remaining_Silver int NOT NULL CHECK (Seats_Remaining_Silver >= 0),Class_Cost_Gold int NOT NULL,Class_Cost_Silver int NOT NULL,T_ID varchar(5) NOT NULL,Movie_ID varchar(5) NOT NULL,Primary Key(Show_ID),Foreign Key (T_ID) REFERENCES Theater(Theatre_ID) ON DELETE CASCADE ON UPDATE CASCADE,Foreign Key (Movie_ID) REFERENCES Movie(Movie_ID) ON DELETE CASCADE ON UPDATE CASCADE);")


def Add_Show():
    cur.execute("Insert into Shows values ('S001T01', '09:00:00', '04/04/2018', 20, 60, 400, 350,'T01','001'),('S001T04', '15:00:00', '04/04/2018', 20, 60, 400, 350, 'T04', '001'),('S002T02', '10:00:00', '04/04/2018', 20, 60, 400, 350, 'T02', '002'),('S002T05', '19:00:00', '04/04/2018', 20, 60, 400, 350, 'T05','002'),('S003T03', '06:00:00', '04/04/2018', 22, 64, 395, 325, 'T03', '003'),('S003T06', '22:00:00', '04/04/2018', 22, 64, 395, 325, 'T06', '003'),('S004T07', '10:00:00', '04/04/2018', 20, 60, 400, 350, 'T07', '004'),('S005T08', '13:00:00', '04/04/2018', 20, 60, 400, 350, 'T08', '005');")
    mydb.commit()

def BookingTable():
    cur.execute("CREATE TABLE IF NOT EXISTS Booking(Booking_ID varchar(10),No_of_Tickets int NOT NULL,Total_Cost int NOT NULL,Card_Number varchar(19),Name_on_card varchar(21),U_ID varchar(5),S1_ID varchar(10),Foreign Key (U_ID) REFERENCES Web_User (Web_User_ID) ON DELETE CASCADE ON UPDATE CASCADE,Foreign Key (S1_ID) REFERENCES Shows(Show_ID) ON DELETE CASCADE ON UPDATE CASCADE,Primary Key(Booking_ID));")

def Add_Booking(Booking_ID ,No_Tickets, Total_Cost ,Card_No ,Name_on_card,selectshow,Web_User_ID):
    cur.execute('INSERT INTO Booking VALUES (%s,%s,%s,%s,%s,%s,%s);',
              (Booking_ID ,No_Tickets, Total_Cost ,Card_No ,Name_on_card,selectshow,Web_User_ID))
    mydb.commit()

