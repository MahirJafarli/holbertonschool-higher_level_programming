-- Converts hbtn_0c_0 database, first_table, and name field to UTF8
-- The specific encoding is utf8mb4 with utf8mb4_unicode_ci collation

-- Convert the database
USE `hbtn_0c_0`;
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the specific field (Note: CONVERT TO above usually handles this, 
-- but this explicitly ensures the field 'name' is updated)
ALTER TABLE `first_table` MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
