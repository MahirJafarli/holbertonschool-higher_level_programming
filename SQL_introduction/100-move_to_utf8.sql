-- Converts hbtn_0c_0 database, first_table, and name field to UTF8
-- The script handles the database, then the table conversion

-- Convert the database
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Switch to the database
USE `hbtn_0c_0`;

-- Convert the table and all its string columns (including 'name')
-- CONVERT TO changes the table default AND all existing columns
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
