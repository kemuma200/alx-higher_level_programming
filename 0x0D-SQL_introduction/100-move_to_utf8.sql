-- script that converts hbtn_0c_0 database to UTF8
11;rgb:0000/0000/0000-- alter database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- alter table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- alter field
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8mb4_unicode_ci;
