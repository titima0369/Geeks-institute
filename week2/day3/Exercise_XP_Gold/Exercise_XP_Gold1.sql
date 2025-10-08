-- Exercise 2 – Happy Halloween
-- Assumes schema similar to Sakila DVD rental database

------------------------------------------------------------
-- 1. How many stores there are, and in which city/country
------------------------------------------------------------
SELECT s.store_id,
       c.city,
       co.country
FROM store s
JOIN address a   ON s.address_id = a.address_id
JOIN city c      ON a.city_id = c.city_id
JOIN country co  ON c.country_id = co.country_id;

------------------------------------------------------------
-- 2. Total viewing time (minutes) in each store
--    Only DVDs that have been returned
------------------------------------------------------------
SELECT i.store_id,
       SUM(f.length) AS total_minutes,
       SUM(f.length)/60.0 AS total_hours,
       SUM(f.length)/60.0/24.0 AS total_days
FROM inventory i
JOIN film f ON i.film_id = f.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL
GROUP BY i.store_id;

------------------------------------------------------------
-- 3. List of all customers in the cities where stores are located
------------------------------------------------------------
SELECT DISTINCT cu.customer_id,
       cu.first_name,
       cu.last_name,
       ci.city
FROM customer cu
JOIN address a ON cu.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city_id IN (
    SELECT a2.city_id
    FROM store s
    JOIN address a2 ON s.address_id = a2.address_id
);

------------------------------------------------------------
-- 4. List of all customers in the countries where stores are located
------------------------------------------------------------
SELECT DISTINCT cu.customer_id,
       cu.first_name,
       cu.last_name,
       co.country
FROM customer cu
JOIN address a ON cu.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country_id IN (
    SELECT ci2.country_id
    FROM store s
    JOIN address a2 ON s.address_id = a2.address_id
    JOIN city ci2 ON a2.city_id = ci2.city_id
);

------------------------------------------------------------
-- 5. Safe list of films (exclude Horror and titles/descriptions 
--    with beast/monster/ghost/dead/zombie/undead).
--    Sum of safe viewing time
------------------------------------------------------------
-- Safe films table (using CHECK constraint)
CREATE TABLE safe_film AS
SELECT f.film_id,
       f.title,
       f.description,
       f.length
FROM film f
WHERE f.film_id NOT IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Horror'
)
AND f.title NOT ILIKE '%beast%'
AND f.title NOT ILIKE '%monster%'
AND f.title NOT ILIKE '%ghost%'
AND f.title NOT ILIKE '%dead%'
AND f.title NOT ILIKE '%zombie%'
AND f.title NOT ILIKE '%undead%'
AND f.description NOT ILIKE '%beast%'
AND f.description NOT ILIKE '%monster%'
AND f.description NOT ILIKE '%ghost%'
AND f.description NOT ILIKE '%dead%'
AND f.description NOT ILIKE '%zombie%'
AND f.description NOT ILIKE '%undead%';

-- Constraint to keep table clean
ALTER TABLE safe_film
  ADD CONSTRAINT chk_safe
  CHECK ( title NOT ILIKE '%beast%'
          AND title NOT ILIKE '%monster%'
          AND title NOT ILIKE '%ghost%'
          AND title NOT ILIKE '%dead%'
          AND title NOT ILIKE '%zombie%'
          AND title NOT ILIKE '%undead%' );

-- Total safe viewing time
SELECT SUM(length) AS total_minutes,
       SUM(length)/60.0 AS total_hours,
       SUM(length)/60.0/24.0 AS total_days
FROM safe_film;

------------------------------------------------------------
-- 6. General (all films) viewing time in minutes/hours/days
------------------------------------------------------------
SELECT SUM(length) AS total_minutes,
       SUM(length)/60.0 AS total_hours,
       SUM(length)/60.0/24.0 AS total_days
FROM film;
