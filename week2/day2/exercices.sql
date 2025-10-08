-- ex1
-- SELECT * 
-- FROM items
-- ORDER BY price ASC;

-- SELECT * 
-- FROM items
-- WHERE price >= 80
-- ORDER BY price DESC;


-- SELECT first_name, last_name
-- FROM customers
-- ORDER BY first_name ASC
-- LIMIT 3;

-- SELECT last_name
-- FROM customers
-- ORDER BY last_name DESC;

-- ex2
-- 1)Select all columns from the customer table
SELECT * 
FROM customer;

-- 2)Display names with alias "full_name"
SELECT first_name || ' ' || last_name AS full_name
FROM customer;

-- 3)All unique account creation dates
SELECT DISTINCT create_date
FROM customer;

-- 4)All customer details ordered by first name (descending)
SELECT * 
FROM customer
ORDER BY first_name DESC;

-- 5)Film ID, title, description, release year, rental rate (ascending rental rate)
SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

-- 6)Address + phone of all customers living in Texas
SELECT address, phone
FROM address
WHERE district = 'Texas';

-- 7)Movie details where id = 15 or 150
SELECT *
FROM film
WHERE film_id IN (15, 150);

-- 8)Check if your favorite movie exists (example: 'ACADEMY DINOSAUR')
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'ACADEMY DINOSAUR';

-- 9)Movies starting with first two letters of favorite movie (example: 'AC')
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE 'AC%';

-- 10)Find 10 cheapest movies
SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 10;

-- 11)Next 10 cheapest movies (without LIMIT, using OFFSET)
SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
OFFSET 10 FETCH NEXT 10 ROWS ONLY;

-- 12)Join customer and payment tables
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
INNER JOIN payment p 
ON c.customer_id = p.customer_id
ORDER BY c.customer_id;

-- 13)Movies not in inventory
SELECT f.film_id, f.title
FROM film f
LEFT JOIN inventory i 
ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL;

-- 14)Find which city is in which country
SELECT ci.city, co.country
FROM city ci
INNER JOIN country co
ON ci.country_id = co.country_id;

-- 15)BONUS: Sellers performance (staff → customers’ payments)
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
INNER JOIN payment p
ON c.customer_id = p.customer_id
ORDER BY p.staff_id;
