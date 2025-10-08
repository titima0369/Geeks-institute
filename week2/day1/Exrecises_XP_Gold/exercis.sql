USE bootcamp;

-- 1. Fetch the first four students ordered alphabetically by last_name
SELECT first_name, last_name, birth_date
FROM students
ORDER BY last_name ASC
LIMIT 4;

-- 2. Fetch the details of the youngest student
SELECT first_name, last_name, birth_date
FROM students
ORDER BY birth_date DESC
LIMIT 1;

-- 3. Fetch three students skipping the first two
SELECT first_name, last_name, birth_date
FROM students
ORDER BY id ASC
LIMIT 3 OFFSET 2;
