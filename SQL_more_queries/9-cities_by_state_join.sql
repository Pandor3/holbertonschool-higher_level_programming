-- 9. This script will list all cities contained in the database named hbtn_0d_usa
SELECT cities.id, cities.name, states.name 
FROM cities, states 
WHERE cities.state_id = states.id 
ORDER BY cities.id ASC;