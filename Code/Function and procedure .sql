--FUNCTION
USE movie_booking_tool;
DELIMITER $$
CREATE FUNCTION count_booking(ticket int)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
DECLARE VALUE varchar(50);
IF ticket > 10 then
set VALUE="Your Limit is limit is over. Retry Post One Month";
 ELSE
set VALUE ="Can Purchase ticket";
 end if;
 return value;
END$$
DELIMITER ;

with t as (Select U_ID,sum(No_of_Tickets) as count from booking group by U_ID )
select U_ID, count_booking(count) as Validate,count as ticket_purchased from t;

--PROCEDURE
USE movie_booking_tool;
SET FOREIGN_KEY_CHECKS=0;
DELIMITER //
CREATE PROCEDURE delete_old_date()
BEGIN
declare curdate date;
set curdate=curdate();
DELETE FROM shows
WHERE datediff(Show_Date,curdate)<0;
END //
DELIMITER ;
CALL delete_old_date;
