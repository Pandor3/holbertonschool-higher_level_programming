-- 1. This script will create a server user named user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* to 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;