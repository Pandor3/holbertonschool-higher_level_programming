-- 8. This script will list all the cities of California that can be found in the database named hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
