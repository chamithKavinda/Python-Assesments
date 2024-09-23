CREATE DATABASE python_db_configure;

USE python_db_configure;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);