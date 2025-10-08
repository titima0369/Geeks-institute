-- Create FirstTab
CREATE TABLE FirstTab (
     id INTEGER, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

-- Create SecondTab
CREATE TABLE SecondTab (
    id INTEGER
);

INSERT INTO SecondTab VALUES
(5),
(NULL);

-- Q1
-- Expected result: 0
SELECT COUNT(*) AS Q1_Result
FROM FirstTab AS ft
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id IS NULL
);

-- Q2
-- Expected result: 2
SELECT COUNT(*) AS Q2_Result
FROM FirstTab AS ft
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id = 5
);

-- Q3
-- Expected result: 0
SELECT COUNT(*) AS Q3_Result
FROM FirstTab AS ft
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab
);

-- Q4
-- Expected result: 2
SELECT COUNT(*) AS Q4_Result
FROM FirstTab AS ft
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id IS NOT NULL
);
