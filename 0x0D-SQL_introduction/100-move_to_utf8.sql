-- script that converts hbtn_0c_0 database to UTF8
--modify database
--modify table
--modify fiedl name

ALTER DATABASE htbn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CONVERT TO CHARACTER SET utmb8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
