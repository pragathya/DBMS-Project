
CREATE Table Web_user(
Web_User_ID varchar(5),
First_Name varchar(15), 
Last_Name varchar(20),
Email_ID varchar(30),
Age int,
Phone_Number varchar(10) NOT NULL, 
Primary Key(Web_User_ID));

Create Table Movie(
Movie_ID varchar(5),
Name varchar(30) NOT NULL,
Language varchar(10),
Genre varchar(20),
Target_Audience varchar(5),
Primary Key(Movie_ID));

Create Table Theatre(
Theatre_ID varchar(5),
Name_of_Theatre varchar(30) NOT NULL,
No_of_Screens int,
Area varchar(30),
M_ID varchar(10),
Foreign Key (M_ID) REFERENCES Movie (Movie_ID) ON DELETE CASCADE ON UPDATE CASCADE,
Primary Key(Theatre_ID));

CREATE Table Shows(				
Show_ID varchar(10),
Show_Time time NOT NULL,
Show_Date date NOT NULL,				
Seats_Remaining_Gold int NOT NULL CHECK (Seats_Remaining_Gold >= 0),
Seats_Remaining_Silver int NOT NULL CHECK (Seats_Remaining_Silver >= 0),
Class_Cost_Gold int NOT NULL,
Class_Cost_Silver int NOT NULL,
M_ID varchar(5) NOT NULL,
T_ID varchar(5) NOT NULL,
Foreign Key (M_ID) REFERENCES Movie(Movie_ID) ON DELETE CASCADE ON UPDATE CASCADE,
Foreign Key (T_ID) REFERENCES Theatre(Theatre_ID) ON DELETE CASCADE ON UPDATE CASCADE,
Primary Key(Show_ID));

CREATE Table Booking(
Booking_ID varchar(10),
No_of_Tickets int NOT NULL,
Total_Cost int NOT NULL,                                           
Card_Number varchar(19),
Name_on_card varchar(21),
U_ID varchar(5),
S_ID varchar(10),
Foreign Key (U_ID) REFERENCES Web_User (Web_User_ID) ON DELETE CASCADE ON UPDATE CASCADE,
Foreign Key (S_ID) REFERENCES Shows(Show_ID) ON DELETE CASCADE ON UPDATE CASCADE,
Primary Key(Booking_ID));

CREATE Table Ticket(
Ticket_ID varchar(20),
B_ID varchar(10),
Class varchar(3) NOT NULL,
Price int NOT NULL,
Foreign Key(B_ID) REFERENCES Booking(Booking_ID) ON DELETE CASCADE,
Primary Key(Ticket_ID));