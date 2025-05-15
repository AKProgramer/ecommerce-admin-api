-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS inventory_history;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;

-- Create Categories Table
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

-- Create Products Table
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Create Inventory Table
CREATE TABLE inventory (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create Inventory History Table
CREATE TABLE inventory_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    inventory_id INT,
    product_id INT,
    change_amount INT,
    reason VARCHAR(255),
    changed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inventory_id) REFERENCES inventory(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create Sales Table
CREATE TABLE sales (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    quantity INT NOT NULL,
    total_price FLOAT NOT NULL,
    sale_date DATETIME NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert Categories
INSERT INTO categories (name) VALUES
('Electronics'),
('Books'),
('Clothing'),
('Home Appliances'),
('Toys');

-- Insert Products
INSERT INTO products (name, description, price, category_id) VALUES
('Smartphone', 'Latest model smartphone', 699.99, 1),
('Laptop', 'High-performance laptop', 1299.99, 1),
('Novel', 'Bestselling novel', 19.99, 2),
('T-shirt', 'Comfortable cotton t-shirt', 9.99, 3),
('Blender', 'High-speed blender', 49.99, 4),
('Action Figure', 'Popular superhero action figure', 14.99, 5);

-- Insert Inventory
INSERT INTO inventory (product_id, quantity) VALUES
(1, 50),
(2, 30),
(3, 100),
(4, 200),
(5, 25),
(6, 150);

-- Insert Inventory History
INSERT INTO inventory_history (inventory_id, product_id, change_amount, reason, changed_at) VALUES
(1, 1, 10, 'Initial stock', '2025-04-30 09:00:00'),
(1, 1, -2, 'Sale', '2025-05-01 10:05:00'),
(2, 2, 30, 'Initial stock', '2025-04-30 09:10:00'),
(3, 3, 100, 'Initial stock', '2025-04-30 09:20:00'),
(4, 4, 200, 'Initial stock', '2025-04-30 09:30:00'),
(5, 5, 25, 'Initial stock', '2025-04-30 09:40:00'),
(6, 6, 150, 'Initial stock', '2025-04-30 09:50:00'),
(6, 6, -3, 'Sale', '2025-05-05 15:25:00');

-- Insert Sales
INSERT INTO sales (product_id, quantity, total_price, sale_date) VALUES
(1, 2, 1399.98, '2025-05-01 10:00:00'),
(3, 1, 19.99, '2025-05-02 14:30:00'),
(4, 5, 49.95, '2025-05-03 16:45:00'),
(5, 1, 49.99, '2025-05-04 12:00:00'),
(6, 3, 44.97, '2025-05-05 15:20:00');
