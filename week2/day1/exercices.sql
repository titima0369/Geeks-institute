-- Exercise 1 : Items and Customers

CREATE DATABASE public;

\c public;

-- 2) 
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    price INT
);

-- 3)
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- 4) 
INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

-- 5) 
INSERT INTO customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');



-- A)
SELECT * FROM items;

-- B) 
SELECT * 
FROM items
WHERE price > 80;

-- C) 
SELECT * 
FROM items
WHERE price <= 300;

-- D)
SELECT * 
FROM customers
WHERE last_name = 'Smith';


-- E)
SELECT * 
FROM customers
WHERE last_name = 'Jones';

-- F)
SELECT * 
FROM customers
WHERE first_name <> 'Scott';
