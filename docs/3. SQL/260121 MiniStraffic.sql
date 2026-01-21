CREATE TABLE storage.local_Amenities(
	station_id 			VARCHAR(10)		primary key,
	station_name 		VARCHAR(100)	not null,
	line_name 			VARCHAR(10)		not null,
	elevator 			VARCHAR(10)		not null,
	wheelchairlift 		VARCHAR(10)		not null,
	parking 			VARCHAR(10)		not null,
	complaint 			VARCHAR(10)		not null,
	exchange 			VARCHAR(10)		not null,
	trainreservation 	VARCHAR(10)		not null,
	culturalspace 		VARCHAR(10)		not null,
	meeting 			VARCHAR(10)		not null,
	lactation 			VARCHAR(10)		not null,
	created_at 			TIMESTAMP 		DEFAULT CURRENT_TIMESTAMP
);

