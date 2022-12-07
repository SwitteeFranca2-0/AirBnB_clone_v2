-- creating a new test user

CREATE DATABASE IF NOT EXISTS hbtn_test_db;
CREATE USER IF NOT EXISTS hbtn_test@localhost IDENTIFIED BY 'hbtn_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_test'@'localhost';
