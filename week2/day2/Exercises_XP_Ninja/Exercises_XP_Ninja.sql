-- 1. Fetch the last 2 customers in alphabetical order (A-Z) – exclude 'id'
SELECT first_name, last_name
FROM customers
ORDER BY last_name ASC
LIMIT 2 OFFSET (
  SELECT COUNT(*) - 2 FROM customers
);


-- 2. Delete all purchases made by Scott
DELETE FROM purchases
WHERE customer_id = (
  SELECT id FROM customers WHERE first_name = 'Scott'
);


-- 3. Check if Scott still exists in the customers table
SELECT * 
FROM customers 
WHERE first_name = 'Scott';


-- 4. Find all purchases with Scott showing as blank
-- Use LEFT JOIN (keeps all purchases, even if customer deleted)
SELECT p.id AS purchase_id,
       p.item,
       c.first_name,
       c.last_name
FROM purchases p
LEFT JOIN customers c ON p.customer_id = c.id;


-- 5. Find all purchases without Scott’s order
-- Use INNER JOIN (only matches existing customers)
SELECT p.id AS purchase_id,
       p.item,
       c.first_name,
       c.last_name
FROM purchases p
INNER JOIN customers c ON p.customer_id = c.id;
