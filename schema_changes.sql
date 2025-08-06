-- 1. Create database if missing
CREATE DATABASE IF NOT EXISTS usersdb;
USE usersdb;

-- 2. Create users table
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(100) NOT NULL
);
