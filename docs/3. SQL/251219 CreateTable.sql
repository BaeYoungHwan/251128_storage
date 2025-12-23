CREATE TABLE storage.local(
	local_id 		VARCHAR(10) 	primary key,
	local_name 		VARCHAR(100) 	not null,
	station_id 		VARCHAR(10)		not null,
	station_name 	VARCHAR(100)	not null,
	line_name 		VARCHAR(10)		not null,
	created_at 		TIMESTAMP 		DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE storage.locker_inventory (
    inventory_id 	SERIAL		 	PRIMARY KEY,
    line_name 		VARCHAR(10)		not null,
	local_id 		VARCHAR(10) 	not null,  
    local_name 		VARCHAR(100)	not null,
    local_small		int,
	local_middle	int,
	local_large		int,
    created_at 		TIMESTAMP 		DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (local_id) REFERENCES storage.local(local_id)
	
);

CREATE TABLE storage.locker_usage (
    usage_id 		SERIAL 			PRIMARY KEY,
    station_name 	VARCHAR(100) 	NOT NULL,
	local_id 		VARCHAR(10)		NOT NULL,
	local_name 		VARCHAR(100)	not null,
	able_small		int,
	able_middle		int,
	able_large		int,
    observed_at 	TIMESTAMP NOT NULL,
    created_at 		TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (local_id) REFERENCES storage.local(local_id)
);

--drop table storage.local
--drop table storage.local
--drop table storage.locker_inventory
select * from "storage".locker_inventory order by locker_inventory.inventory_id;
select * from "storage".locker_inventory where local_name like '종합&';
select * from "storage".locker_usage where observed_at > '2025-12-22 17:00:00' and observed_at < '2025-12-22 17:30:00';
select * from "storage"."local" where local_name like '충정로%';
select * from "storage".locker_usage where local_name like '올림픽%';
select * from "storage".locker_inventory ;
select * from "storage"."local" where local_id = 'TL737';
select * from "storage".locker_usage;

Begin

TRUNCATE storage.locker_inventory RESTART IDENTITY;

select * from "storage".locker_inventory where local_name = '상도';


Rollback






SELECT
    "storage"."local".local_id,
    "storage"."local".local_name AS updated_main_name,
    "storage".locker_usage.local_name AS original_fk_name,
    REGEXP_REPLACE("storage".locker_usage.local_name, '^\d+호선\s*', '') AS preview_updated_fk_name
FROM  "storage".locker_usage
JOIN  "storage"."local" ON "storage".locker_usage.local_id = "storage"."local".local_id
WHERE "storage".locker_usage.local_name ~ '^\d+호선\s*';

/*
BEGIN;

UPDATE "storage"."local"
SET local_name = REGEXP_REPLACE(local_name, '^\d+호선\s*', '')
WHERE local_name ~ '^\d+호선\s*';

UPDATE "storage".locker_usage
SET local_name = "storage"."local".local_name
FROM "storage"."local"
WHERE "storage".locker_usage.local_id = "storage"."local".local_id
  AND "storage".locker_usage.local_name ~ '^\d+호선\s*'; 

COMMIT;

ROLLBACK;

UPDATE stations
SET station_name = REGEXP_REPLACE(station_name, '^\d+호선\s*', '')
WHERE station_name ~ '^\d+호선\s*';

Alter Table storage.locker_usage
add constraint unique_local_usage
Unique (local_id, observed_at);
*/

select station_name, local_name from "storage".locker_usage where able_large = 0 and able_middle = 0 and able_small =0 and observed_at > '2025-12-22 17:13';

INSERT INTO storage.locker_usage
    (station_name, local_id, local_name, able_small, able_middle, able_large, observed_at)
    VALUES ('청량리',' :local_id', :local_name, :able_small, :able_middle, :able_large, :observed_at)