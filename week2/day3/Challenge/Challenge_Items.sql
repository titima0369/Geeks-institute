-- Create Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create Product Orders table
CREATE TABLE product_orders (
    id SERIAL PRIMARY KEY,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT,  -- each order belongs to one user
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create Items table
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL, -- price column
    order_id INT, -- each item belongs to one order
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES product_orders(id) ON DELETE CASCADE
);

-- Function to get total price of a given order
CREATE OR REPLACE FUNCTION get_order_total(orderId INT)
RETURNS NUMERIC AS $$
    SELECT COALESCE(SUM(price), 0)
    FROM items
    WHERE order_id = orderId;
$$ LANGUAGE SQL;

-- Function to get total price of a given order for a given user
CREATE OR REPLACE FUNCTION get_user_order_total(userId INT, orderId INT)
RETURNS NUMERIC AS $$
    SELECT COALESCE(SUM(i.price), 0)
    FROM items i
    JOIN product_orders o ON i.order_id = o.id
    WHERE o.id = orderId AND o.user_id = userId;
$$ LANGUAGE SQL;

-- Insert Users
INSERT INTO users (name, email) VALUES
('Brahim', 'brahim@example.com'),
('Sara', 'sara@example.com');

-- Insert Orders
INSERT INTO product_orders (user_id) VALUES
(1),  -- Order for Brahim
(1),  -- Another order for Brahim
(2);  -- Order for Sara

-- Insert Items
INSERT INTO items (name, price, order_id) VALUES
('Laptop', 8000.00, 1),
('Mouse', 150.00, 1),
('Keyboard', 300.00, 2),
('Monitor', 1200.00, 2),
('Phone', 5000.00, 3);


-- Example Queries
-- Total for order 1
SELECT get_order_total(1);

-- Total for order 2 of user 1
SELECT get_user_order_total(1, 2);

-- Total for order 3 of user 2
SELECT get_user_order_total(2, 3);