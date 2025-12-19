CREATE TABLE storage.local(
	local_id 		VARCHAR(10) 	primary key,
	local_name 		VARCHAR(100) 	not null,
	station_id 		VARCHAR(10)		not null,
	station_name 	VARCHAR(100)	not null,
	line_name 		VARCHAR(10)		not null,
	created_at 		TIMESTAMP 		DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE storage.locker_inventory (
    inventory_id 	SERIAL 			PRIMARY KEY,
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




select * from "storage"."local";
select * from "storage".locker_inventory;
select * from "storage".locker_usage where station_name = '홍대입구';
select * from "storage"."local" where local_name like '충정로%';




drop table storage.local;
drop table storage.locker_usage;
drop table storage.locker_inventory;


ALTER TABLE storage.locker_usage
ADD CONSTRAINT unique_local_usage
UNIQUE (local_id, observed_at);


INSERT INTO storage.locker_usage
    (station_name, local_id, local_name, able_small, able_middle, able_large, observed_at)
    VALUES ('청량리','sdsd', 'e', 1, 2, 3, '2025-12-19 15:56:00.484762')