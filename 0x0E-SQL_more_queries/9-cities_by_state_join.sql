-- lists all cities contained in the database hbtn_0d_usa.
SELECT id, name FROM cities, name FROM states ORDER BY id ASC;
SELECT cities.id, cities.name (SELECT states.name FROM states WHERE states.id = cities.state_id) FROM cities ORDER BY cities.id ASC;
