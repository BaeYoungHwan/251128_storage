-- SCHEMA: storage

-- DROP SCHEMA IF EXISTS storage ;

CREATE SCHEMA IF NOT EXISTS storage
    AUTHORIZATION postgres;

COMMENT ON SCHEMA storage
    IS 'for storage project';


	-- 

	CREATE TABLE stations (
    station_id SERIAL PRIMARY KEY,
    station_name VARCHAR(100) NOT NULL,
    line_name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (station_name)
);


CREATE TABLE locker_usage (
    usage_id SERIAL PRIMARY KEY,
    station_id INTEGER NOT NULL REFERENCES stations(station_id),
    total_lockers INTEGER NOT NULL,
    used_lockers INTEGER NOT NULL,
    available_lockers INTEGER NOT NULL,
    observed_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (station_id, observed_at)
);

drop table stations;
drop table locker_usage;


show search_path;

set search_path To "storage", public;



select * from stations;


