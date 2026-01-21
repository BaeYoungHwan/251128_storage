-- CREATE TABLE storage.local_Amenities(
-- 	station_id 			VARCHAR(10)		primary key,
-- 	station_name 		VARCHAR(100)	not null,
-- 	line_name 			VARCHAR(10)		not null,
-- 	elevator 			VARCHAR(10)		not null,
-- 	wheelchairlift 		VARCHAR(10)		not null,
-- 	parking 			VARCHAR(10)		not null,
-- 	complaint 			VARCHAR(10)		not null,
-- 	exchange 			VARCHAR(10)		not null,
-- 	trainreservation 	VARCHAR(10)		not null,
-- 	culturalspace 		VARCHAR(10)		not null,
-- 	meeting 			VARCHAR(10)		not null,
-- 	lactation 			VARCHAR(10)		not null,
-- 	created_at 			TIMESTAMP 		DEFAULT CURRENT_TIMESTAMP
-- );

drop table storage.Amenities;

select * from storage.local_amenities;

select * from storage.local

CREATE TABLE storage.user(
	user_id				VARCHAR(20)		primary key,
	user_pw				VARCHAR(10)		not null,
	station_id 			VARCHAR(10)		not null,
	station_name 		VARCHAR(100)	not null,
	line_name 			VARCHAR(10)		not null,
	user_name			VARCHAR(10)		not null,
	user_email			VARCHAR(20),
	auth				VARCHAR(10)		not null
	
);
