-- 9. This script will list all cities contained in the database named hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities ORDER BY cities.id ASC;