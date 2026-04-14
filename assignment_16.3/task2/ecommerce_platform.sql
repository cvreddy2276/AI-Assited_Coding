-- E-commerce Platform Schema and Queries
-- Using SQLite3

-- Users table
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at DATE DEFAULT CURRENT_DATE,
    phone TEXT,
    shipping_address TEXT
);

-- Products table
CREATE TABLE Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sku TEXT NOT NULL UNIQUE,
    category TEXT,
    price REAL NOT NULL CHECK (price >= 0),
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0)
);

-- Orders table
CREATE TABLE Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT NOT NULL DEFAULT 'pending',
    shipping_address TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    CHECK (status IN ('pending', 'confirmed', 'shipped', 'delivered', 'cancelled'))
);

-- OrderDetails table
CREATE TABLE OrderDetails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL CHECK (unit_price >= 0),
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (product_id) REFERENCES Products(id),
    UNIQUE(order_id, product_id)
);

-- Query 1: Retrieve all orders by a user
-- Replace ? with the actual user ID
SELECT o.id AS order_id,
       o.order_date,
       o.status,
       p.id AS product_id,
       p.name AS product_name,
       od.quantity,
       od.unit_price,
       (od.quantity * od.unit_price) AS line_total
FROM Orders o
JOIN OrderDetails od ON o.id = od.order_id
JOIN Products p ON od.product_id = p.id
WHERE o.user_id = ?
ORDER BY o.order_date DESC, o.id, p.name;

-- Query 2: Find the most purchased product
SELECT p.id AS product_id,
       p.name AS product_name,
       SUM(od.quantity) AS total_quantity_sold
FROM OrderDetails od
JOIN Products p ON od.product_id = p.id
GROUP BY p.id, p.name
ORDER BY total_quantity_sold DESC
LIMIT 1;

-- Query 3: Calculate total revenue in a given month
-- Replace ? with the year-month string like '2026-04'
SELECT strftime('%Y-%m', o.order_date) AS order_month,
       SUM(od.quantity * od.unit_price) AS total_revenue
FROM Orders o
JOIN OrderDetails od ON o.id = od.order_id
WHERE strftime('%Y-%m', o.order_date) = ?
GROUP BY order_month;

-- Improvements for normalization and query optimization:
-- 1. Normalize product categories into a separate Category table if categories have attributes of their own.
-- 2. Normalize order status values into a lookup table to avoid repeated string values and make status changes easier.
-- 3. Add indexes on Orders(user_id), OrderDetails(order_id), OrderDetails(product_id), and Orders(order_date) for query performance.
-- 4. Store order totals only if maintained by triggers or application logic; otherwise calculate from OrderDetails to avoid denormalization anomalies.
-- 5. Consider a dedicated CustomerAddresses table for multiple shipping addresses per user.
