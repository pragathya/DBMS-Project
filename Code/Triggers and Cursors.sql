--TRIGGERS
USE movie_booking_tool;
SET FOREIGN_KEY_CHECKS=0;
DELIMITER $$
CREATE TRIGGER check_age
AFTER INSERT
ON web_user FOR EACH ROW
BEGIN
 DECLARE error_msg VARCHAR(200);
 declare count int;
 SET error_msg = ('Under age');
 IF (select Age from web_user where Web_User_ID = new.Web_User_ID) < '14' THEN
 SIGNAL SQLSTATE '45000'
 SET MESSAGE_TEXT = error_msg;
 END IF;
END $$
DELIMITER ;
insert into web_user values ('U14','Ann','Joseph','aj@gmail.com','11','6574389012');

--CURSORS
use movie_booking_tool;
DELIMITER $$
CREATE PROCEDURE createEmailList_ (
	INOUT emailList varchar(4000)
)
BEGIN
	DECLARE finished INTEGER DEFAULT 0;
	DECLARE emailAddress varchar(100) DEFAULT "";

	-- declare cursor for employee email
	DEClARE curEmail 
		CURSOR FOR 
			SELECT Email_ID FROM web_user;

	-- declare NOT FOUND handler
	DECLARE CONTINUE HANDLER 
        FOR NOT FOUND SET finished = 1;

	OPEN curEmail;

	getEmail: LOOP
		FETCH curEmail INTO emailAddress;
		IF finished = 1 THEN 
			LEAVE getEmail;
		END IF;
		-- build email list
		SET emailList = CONCAT(emailAddress,";",emailList);
	END LOOP getEmail;
	CLOSE curEmail;

END$$
DELIMITER ;

SET @emailList = ""; 
CALL createEmailList_(@emailList); 
SELECT @emailList;

