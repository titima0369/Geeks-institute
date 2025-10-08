
-- 1. Use UPDATE to change the language of some films
UPDATE film SET language_id = (SELECT language_id FROM language WHERE name = 'French')
WHERE film_id < 5;

-- 2. Which foreign keys are defined for the customer table?
-- (Query to show foreign keys of table customer)
SELECT conname, conrelid::regclass AS table_name, confrelid::regclass AS referenced_table
FROM pg_constraint
WHERE conrelid = 'customer'::regclass AND contype = 'f';

-- 3. Drop the table customer_review
DROP TABLE IF EXISTS customer_review CASCADE;

-- 4. Find how many rentals are still outstanding
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

-- 5. Find the 30 most expensive outstanding movies
SELECT f.title, f.rental_rate
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30;

-- 6. Your friend wants 4 movies

-- 1st film : sumo wrestler, actor Penelope Monroe
SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.description ILIKE '%sumo wrestler%'
  AND a.first_name = 'Penelope' AND a.last_name = 'Monroe';

-- 2nd film : short documentary (< 1 hour), rated "R"
SELECT title
FROM film
WHERE length < 60 AND rating = 'R';

-- 3rd film : rented by Matthew Mahan, paid > $4.00, returned 28 July - 1 Aug 2005
SELECT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
JOIN payment p ON r.rental_id = p.rental_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND p.amount > 4
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- 4th film : watched by Matthew Mahan, "boat" in title/description, expensive to replace
SELECT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;