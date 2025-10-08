-- 1. Count films by rating
SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating;

-- 2. Get list of movies with rating G or PG-13
SELECT title, rating
FROM film
WHERE rating IN ('G','PG-13');

-- 3. Filter movies under 2 hours and rental_rate < 3.00, sorted alphabetically
SELECT title, rating, length, rental_rate
FROM film
WHERE rating IN ('G','PG-13')
  AND length < 120
  AND rental_rate < 3.00
ORDER BY title;

-- 4. Update a customer's details
UPDATE customer
SET first_name = 'Brahim', last_name = 'Oudra', email = 'oudra.brahim@gmail.com'
WHERE customer_id = 1; -- example ID

-- 5. Update the customer's address
UPDATE address
SET address = '123 Main Street', district='Marrakech'
WHERE address_id = (
    SELECT address_id 
    FROM customer 
    WHERE customer_id = 1
);
