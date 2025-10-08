-- Exercise 1 – DVD Rentals
-- Assumes schema similar to Sakila DVD rental database

------------------------------------------------------------
-- 1. Retrieve all films with rating G or PG that are not rented
------------------------------------------------------------
SELECT f.film_id,
       f.title,
       f.rating,
       f.length
FROM film f
JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE f.rating IN ('G','PG')
  AND (r.rental_id IS NULL OR r.return_date IS NOT NULL);

------------------------------------------------------------
-- 2. Create a waiting list table for children's movies
--    Python program will manage inserting/removing rows
------------------------------------------------------------
CREATE TABLE childrens_waiting_list (
    waiting_id SERIAL PRIMARY KEY,
    film_id INT NOT NULL,
    child_name VARCHAR(100) NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_child_film FOREIGN KEY (film_id) REFERENCES film(film_id)
);

-- Explanation:
-- References needed: film_id (from film table).
-- Could also reference inventory if we want specific copies, 
-- but film_id is sufficient for children's waiting list.

------------------------------------------------------------
-- 3. Retrieve the number of people waiting for each children's DVD
------------------------------------------------------------
SELECT f.film_id,
       f.title,
       COUNT(cw.waiting_id) AS num_waiting
FROM film f
LEFT JOIN childrens_waiting_list cw ON f.film_id = cw.film_id
WHERE f.rating IN ('G','PG')
GROUP BY f.film_id, f.title
ORDER BY num_waiting DESC;

-- To test:
-- INSERT INTO childrens_waiting_list (film_id, child_name) VALUES (1, 'Alice');
-- INSERT INTO childrens_waiting_list (film_id, child_name) VALUES (1, 'Bob');
-- Then rerun query 3 to see counts.
