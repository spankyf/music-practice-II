CREATE TABLE bass (
	id SERIAL PRIMARY KEY,
	date DATE NOT NULL,
	exercise VARCHAR ( 50 ) NOT NULL,
	duration INTERVAL  NOT NULL,
	instrument VARCHAR(50) NOT NULL
	
);

-- INSERT INTO bass (date,exercise,duration)
-- VALUES ( '10/7/2020', 'scadddl', '200 seconds' );

-- SELECT *
-- FROM bass;

-- DELETE FROM bass
-- WHERE date = '7/10/2020';

-- DROP TABLE bass;