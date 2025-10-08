-- Part I: Create purchases table
CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    item_id INT REFERENCES items(item_id),
    quantity_purchased INT
);

-- Insert purchases using subqueries
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES
( (SELECT customer_id FROM customers WHERE first_name='Scott' AND last_name='Scott'), 
  (SELECT item_id FROM items WHERE item_name='Fan'), 1 ),

( (SELECT customer_id FROM customers WHERE first_name='Melanie' AND last_name='Johnson'), 
  (SELECT item_id FROM items WHERE item_name='Large Desk'), 10 ),

( (SELECT customer_id FROM customers WHERE first_name='Greg' AND last_name='Jones'), 
  (SELECT item_id FROM items WHERE item_name='Small Desk'), 2 );

-- Part II: Queries

-- 1. All purchases
SELECT * FROM purchases;

-- 2. All purchases with customer info
SELECT p.*, c.first_name, c.last_name
FROM purchases p
JOIN customers c ON p.customer_id = c.customer_id;

-- 3. Purchases by customer ID = 5
SELECT * 
FROM purchases
WHERE customer_id = 5;

-- 4. Purchases for Large Desk AND Small Desk
SELECT * 
FROM purchases
WHERE item_id IN (
    SELECT item_id FROM items WHERE item_name IN ('Large Desk','Small Desk')
);

-- 5. Customers who made a purchase, show first_name, last_name, item_name
SELECT c.first_name, c.last_name, i.item_name
FROM purchases p
JOIN customers c ON p.customer_id = c.customer_id
JOIN items i ON p.item_id = i.item_id;

-- 6. Add row referencing customer but no item
-- This will fail if item_id is NOT NULL or foreign key constraint exists
-- Example:
INSERT INTO purchases (customer_id, quantity_purchased)
VALUES (1, 1); -- fails if item_id NOT NULL or FK enforced
