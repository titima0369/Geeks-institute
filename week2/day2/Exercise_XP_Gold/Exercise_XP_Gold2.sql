-- 1. Update twins' birth_dates
UPDATE students
SET birth_date = '1998-02-11'
WHERE last_name = 'Benichou';

-- 2. Change last_name of David
UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name = 'Grez';

-- 3. Delete Lea Benichou
DELETE FROM students
WHERE first_name='Lea' AND last_name='Benichou';

-- 4. Count students
SELECT COUNT(*) AS total_students FROM students;

-- 5. Count students born after 2000-01-01
SELECT COUNT(*) AS born_after_2000
FROM students
WHERE birth_date > '2000-01-01';

-- 6. Add math_grade column
ALTER TABLE students ADD COLUMN math_grade INT;

-- 7. Insert grades
UPDATE students SET math_grade = 80 WHERE id = 1;
UPDATE students SET math_grade = 90 WHERE id IN (2,4);
UPDATE students SET math_grade = 40 WHERE id = 6;

-- 8. Count students with grade > 83
SELECT COUNT(*) AS grade_above_83
FROM students
WHERE math_grade > 83;

-- 9. Add Omer Simpson with grade 70 and same birth_date
INSERT INTO students (first_name, last_name, birth_date, math_grade)
SELECT 'Omer', 'Simpson', birth_date, 70
FROM students
WHERE first_name='Omer' AND last_name='Simpson' LIMIT 1;

-- 10. Count grades per student
SELECT first_name, last_name, COUNT(math_grade) AS total_grade
FROM students
GROUP BY first_name, last_name;

-- 11. Sum of all students' grades
SELECT SUM(math_grade) AS total_grades
FROM students;
