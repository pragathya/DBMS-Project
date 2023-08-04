INSERT INTO web_user VALUES(
 ('U01', 'Tara', 'Frank', 'tr@gmail.com', 19, 9876543210),
 ('U02', 'Lily', 'Mars', 'lm@yahoo.com' , 30, 6543217890),   
 ('U03', 'Shawn', 'Murphy', 'sm@outlook.com' , 24 , 5647382910), 
 ('U04', 'Robert', 'Goldberg', 'rgr@gmail.com' ,38, 8763450912),   
 ('U05', 'Alex', 'Smith', 'als@yahoo.com', 50, 7654000123),  
 ('U06', 'Komal', 'Agarwal', 'komal.agarwal87@gmail.com', 41, 9345687654),  
 ('U07', 'Rahul', 'Raghav', 'rahulrag@gmail.com', 23, 9591990037),  
 ('U08', 'Janice', 'Fernandes', 'janicefernandes@gmail.com', 38, 9325880785), 
 ('U09', 'Nusaiba', 'Mehrunisa', 'nusaibafatima@gmail.com',  24,  8731990037),  
 ('U10', 'Mona', 'Mohammed', 'monaraisa@gmail.com', 23, 9591670037),  
 ('U11', 'Ann', 'Joseph', 'aj@gmail.com', 21, 6574389012));   
 
 Insert into Movie values(
('001', 'Hichki', 'Hindi','Drama/Comedy', 'U/A'),
('002', 'Pacific Rim Uprising',  'English','Fantasy/SciFi', 'U/A'),
('003', 'Strangers : Prey at night','English', 'Horror', 'U/A'),
('004', 'Tomb Raider', 'English','Fantasy/Action', 'A'),
('005', 'Black Panther','English', 'Fantasy/SciFi','U/A'),
('006', 'Peter Rabbit','English', 'Fantasy/Adventure','U/A'),
('007', 'Maze Runner: The Death Cure','English', 'Fantasy/SciFi','U/A'));

Insert into Theatre values(
('T01', 'PVR Cinemas', 4, 'Koramangala, Bangalore'),
('T02', 'INOX Movies', 4, 'Malleshwaram, Bangalore'),
('T03', 'Cinepolis', 3, 'Malleshwaram, Bangalore'),
('T04', 'INOX Movies', 2, 'Rajajinagar, Bangalore'),
('T05', 'PVR Cinemas', 1, 'Indranagar, Bangalore'),
('T06', 'INOX Movies', 2, 'Rajajinagar, Bangalore'),
('T07', 'Cinepolis', 1, ' Whitefield, Bangalore'),
('T08', 'PVR Cinemas', 1, 'Indranagar, Bangalore'));

Insert into shows values(
('S001T01', '09:00:00', '2022-11-28', 20, 60, 400, 350, 'T01', '001'),
('S001T04', '15:00:00', '2022-11-28', 20, 60, 400, 350, 'T04', '001'),
('S002T02', '10:00:00', '2022-11-28', 20, 60, 400, 350, 'T02', '002'),
('S002T05', '19:00:00', '2022-11-28', 20, 60, 400, 350, 'T05', '002'),
('S003T03', '06:00:00', '2022-11-28', 22, 64, 395, 325, 'T03', '003'),
('S003T06', '22:00:00', '2022-11-28', 22, 64, 395, 325, 'T06', '003'),
('S004T07', '10:00:00', '2022-11-28', 20, 60, 400, 350, 'T07', '004'),
('S005T08', '13:00:00', '2022-11-28', 20, 60, 400, 350, 'T08', '005'),
('S101T04', '10:00:00', '2022-11-28', 10, 14, 300, 250, 'T04', '001'),
('S202T05', '07:00:00', '2022-11-28', 10, 14, 300, 250, 'T05', '002'),
('S212T05', '15:00:00', '2022-11-28', 4, 9, 250, 200, 'T05', '002'));

Insert into booking values(
('B01', 1, 400, '45654', 'Tara', 'U01', 'S001T01'),
('B02', 1, 325, '45654', 'Tara', 'U01', 'S003T06'),
('B03', 2, 800, '31654', 'Shawn', 'U03', 'S004T07'),
('B04', 2, 500, '99154', 'Alex', 'U05', 'S202T05'),
('B05', 1, 300, '31112', 'Rahul', 'U07', 'S202T05'),
('B06', 2, 800, '54112', 'Mona',  'U10', 'S001T01'),
('B07', 8, 2400, '54112', 'Mona',  'U10', 'S101T04'),
('B08', 4, 1600, '54112', 'Mona',  'U10', 'S005T08'));

insert into ticket values(
('TB1','B01','Gold',400),
('TB2','B02','Gold',325),
('TB3','B03','Gold',800),
('TB4','B04','Silver',500),
('TB5','B05','Gold',300),
('TB6','B06','Gold',800),
('TB7','B07','Silver',2400),
('TB8','B08','Gold',1600));

 