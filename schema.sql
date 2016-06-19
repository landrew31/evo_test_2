CREATE TABLE adjectives (
	adid SERIAL PRIMARY KEY,
	adjective VARCHAR(30) NOT NULL CHECK (adjective <> '')
);

CREATE TABLE names (
	nid SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL CHECK (name <> ''),
	adid INTEGER REFERENCES adjectives (adid)
);