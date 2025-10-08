
1. Count how many actors are in the table

SELECT COUNT(*) 
FROM actor;


2. Add new actor with some blank fields

INSERT INTO actor (first_name, last_name) 
VALUES ('', '');
-- output 1 row inserted because of the default values 

