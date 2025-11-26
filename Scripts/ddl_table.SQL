/*
=============================================================================
DDL Script: Creates Tables
=============================================================================
Script Purpose:
    This script creates users,products,orders and order_items, dropping existing tables if they already exisit.
=============================================================================    
*/

IF OBJECT_ID('dbo.users','U') IS NOT NULL DROP VIEW dbo.vw_order_totals;
GO

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    signup_date DATE,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    customer_segment VARCHAR(50)
);

IF OBJECT_ID('dbo.products','U') IS NOT NULL DROP VIEW dbo.vw_order_totals;
GO

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(50),
    category VARCHAR(50), 
    subcategory VARCHAR(50),
    price FLOAT,
    cost FLOAT,
    launch_date DATE,
    brand VARCHAR(50)
    );

IF OBJECT_ID('dbo.orders','U') IS NOT NULL DROP VIEW dbo.vw_order_totals;
GO

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    order_status VARCHAR(50),
    payment_method VARCHAR(50),
    shipping_cost FLOAT,
    coupon_code VARCHAR(50)
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    );

IF OBJECT_ID('dbo.order_items','U') IS NOT NULL DROP VIEW dbo.vw_order_totals;
GO

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    discount INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


        

