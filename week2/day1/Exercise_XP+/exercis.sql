-- 1. Create database
CREATE DATABASE bootcamp;

-- 2. Use the database
USE bootcamp;

-- 3. Create table students
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL
);

-- 4. Insert all given rows efficiently
INSERT INTO students (first_name, last_name, birth_date)
VALUES
('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-10-03');

-- 5. Insert your own details (example: John Doe)
INSERT INTO students (first_name, last_name, birth_date)
VALUES ('John', 'Doe', '1995-05-15');


--  Select queries

-- Fetch all of the data
SELECT * FROM students;

-- Fetch all first_names and last_names
SELECT first_name, last_name FROM students;

-- Fetch student with id = 2
SELECT first_name, last_name FROM students WHERE id = 2;

-- Fetch student whose last_name = Benichou AND first_name = Marc
SELECT first_name, last_name FROM students
WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- Fetch students whose last_name = Benichou OR first_name = Marc
SELECT first_name, last_name FROM students
WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- Fetch students whose first_names contain the letter 'a'
SELECT first_name, last_name FROM students
WHERE first_name LIKE '%a%';

-- Fetch students whose first_names start with 'a'
SELECT first_name, last_name FROM students
WHERE first_name LIKE 'a%';

-- Fetch students whose first_names end with 'a'
SELECT first_name, last_name FROM students
WHERE first_name LIKE '%a';

-- Fetch students whose second to last letter of first_name is 'a'
SELECT first_name, last_name FROM students
WHERE first_name LIKE '%a_';

-- Fetch students whose id’s are equal to 1 AND 3
SELECT first_name, last_name FROM students
WHERE id IN (1, 3);

-- Fetch students whose birth_dates are >= 2000-01-01
SELECT * FROM students
WHERE birth_date >= '2000-01-01';
