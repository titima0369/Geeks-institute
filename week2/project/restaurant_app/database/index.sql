-- Categories
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chefs
CREATE TABLE IF NOT EXISTS chefs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Menu Items
CREATE TABLE IF NOT EXISTS menu_items (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    price NUMERIC(10,2) DEFAULT 0,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL
);

-- Association table MenuItem <-> Chef
CREATE TABLE IF NOT EXISTS menu_item_chefs (
    menu_item_id INTEGER REFERENCES menu_items(id) ON DELETE CASCADE,
    chef_id INTEGER REFERENCES chefs(id) ON DELETE CASCADE,
    PRIMARY KEY(menu_item_id, chef_id)
);

-- Orders
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(120) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Order Items
CREATE TABLE IF NOT EXISTS order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    menu_item_id INTEGER REFERENCES menu_items(id) ON DELETE CASCADE,
    quantity INTEGER DEFAULT 1 NOT NULL,
    price_at_order NUMERIC(10,2) NOT NULL
);
