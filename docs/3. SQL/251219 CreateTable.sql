CREATE TABLE storage.local(
	local_id 		VARCHAR(10) 	primary key,
	local_name 		VARCHAR(100) 	not null,
	station_id 		VARCHAR(10)		not null,
	station_name 	VARCHAR(100)	not null,
	line_name 		VARCHAR(10)		not null,
	created_at 		TIMESTAMP 		DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE storage.locker_inventory (
    inventory_id 	VARCHAR(10) 	PRIMARY KEY,
    line_name 		VARCHAR(10)		not null,
	local_id 		VARCHAR(10) 	not null,  
    local_name 		VARCHAR(100)	not null,
    local_small		int,
	local_middle	int,
	local_large		int,
    created_at 		TIMESTAMP 		DEFAULT CURRENT_TIMESTAMP
	FOREIGN KEY (local_id) REFERENCES storage.local(local_id)
	
);
CREATE TABLE storage.locker_usage (
    usage_id 		VARCHAR(10) 	PRIMARY KEY,
    station_name 	VARCHAR(100) 	NOT NULL,
	local_id 		VARCHAR(10)		NOT NULL,
	local_name 		VARCHAR(100)	not null,
	able_small		int,
	able_middle		int,
	able_large		int,
    observed_at 	TIMESTAMP NOT NULL,
    created_at 		TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	FOREIGN KEY (local_id) REFERENCES storage.local(local_id)
);


