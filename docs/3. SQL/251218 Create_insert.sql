
drop table "storage".locker_usage;

CREATE TABLE storage.locker_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(20) UNIQUE NOT NULL
);


CREATE TABLE storage.locker_usage (
    usage_id SERIAL PRIMARY KEY,
    station_id INTEGER REFERENCES storage.stations(station_id),
    type_id INTEGER REFERENCES storage.locker_types(type_id),
    used_count INTEGER NOT NULL,
    observed_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (station_id, type_id, observed_at)
);

CREATE TABLE storage.locker_inventory (
    inventory_id SERIAL PRIMARY KEY,
    station_name VARCHAR(100) NOT NULL,
    line VARCHAR(20),
    locker_name VARCHAR(100),
    locker_type VARCHAR(10),     -- small / medium / large
    total_count INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


select * from "storage".locker_inventory;


INSERT INTO storage.locker_types (type_name)
VALUES
('소형'),
('중형'),
('대형');

drop table "storage".locker_inventory


SELECT * FROM storage.locker_types;