
-- to create a table with primary key- id
CREATE TABLE "Artist" (
	"id"	INTEGER NOT NULL,--not null means that it will have a value
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

--then now we are going to create a Genre table
CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT

)
-- album table that will contain artist id as foreign key
CREATE TABLE Album(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id INTEGER,
	title TEXT
)
-- create track tavle that will have album id and genre id as foreign key
CREATE TABLE Tracks(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT,
	album_id INTEGER,
	genre_id INTEGER,
	len INTEGER,
	rating INTEGER,
	count INTEGER
)
--now insert the values for the artist table for eg
INSERT INTO Artist(name) VALUES('America')
-- do the same for Genre 

--now for album do the below thing
INSERT INTO Album(title,artist_id) VALUES('Who Made Who',2);
INSERT INTO Album(title,artist_id) VALUES('IV',1)

--now for the tracks
insert into Track (title, rating, len, count, album_id, genre_id)
values ('Black Dog', 5, 297, 0, 2, 1);

insert into Track (title, rating, len, count, album_id, genre_id)
values ('Stairway', 5, 482, 0, 2, 1);

insert into Track (title, rating, len, count, album_id, genre_id)
values ('About to Rock', 5, 313, 0, 1, 2);

insert into Track (title, rating, len, count, album_id, genre_id)
values ('Who Made Who', 5, 207, 0, 1, 2)

--now to join the album and artist 
SELECT Album.title, artist.name FROM Album join Artist on Album.artist_id= Artist.id
SELECT Album.title,Album.artist_id,Artist.id, artist.name FROM Album join Artist on Album.artist_id= Artist.id

--to join the track and genre
ELECT Track.title,Genre.name FROM Track join Genre on Track.genre_id= Genre.id

--now join all the tables
SELECT Track.title,Genre.name,Album.title,Artist.name FROM Track join Genre join Album join Artist on Track.genre_id= Genre.id
	and Track.album_id = Album.id and Album.artist_id = Artist.id