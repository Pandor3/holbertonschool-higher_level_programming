-- 1. This script will create a server user named user_0d_1 and give him all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES on *.* TO 'user_0d_1'@'localhost';