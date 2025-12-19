
drop table "storage".locker_usage;

CREATE TABLE storage.locker_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE storage.locker_usage (
    usage_id SERIAL PRIMARY KEY,
    station_name VARCHAR(100) NOT NULL,
    locker_type VARCHAR(10) NOT NULL,  -- small / medium / large
    used_count INTEGER NOT NULL,
    observed_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (station_name, locker_type, observed_at)
);

drop table STORAGE.locker_types;

select * from "storage".stations;
select * from "storage".locker_usage;
select * from "storage".locker_inventory;

select * from "storage".locker_inventory where station_name like '시청%';



CREATE TABLE storage.locker_inventory (
    inventory_id SERIAL PRIMARY KEY,
    station_name VARCHAR(100) NOT NULL,
    line VARCHAR(20),
    locker_name VARCHAR(100),
    locker_type VARCHAR(10),     -- small / medium / large
    total_count INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



INSERT INTO storage.locker_types (type_name)
VALUES
('소형'),
('중형'),
('대형');

drop table "storage".locker_inventory


SELECT * FROM storage.locker_types;