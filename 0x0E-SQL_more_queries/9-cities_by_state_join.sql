-- lists all cities contained in the database
SELECT states.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id ASC;
