--here what we will be doing is we will create two tables seperately
--and then will join them using a junction in this way mamy to many relation will be converted in one to many
--here there can be multiple users taking a particular course and multiple users taking a single course w willl map them
CREATE TABLE Users(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT,
	email TEXT
	)

CREATE TABLE Course(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT,
	)

--here we are making a junction table named members that are going to track user and course
CREATE TABLE Member(
	user_id INTEGER,
	course_id INTEGER,
	role INTEGER,
	PRIMARY KEY (user_id,course_id)
	)

--here we will enter some values in the table
INSERT INTO Users(name,email) VALUES('Jane','jane@gmail.com');
INSERT INTO Users(name,email) VALUES('ED','Ed@gmail.com');
INSERT INTO Users(name,email) VALUES('Sue','Sue@gmail.com');
INSERT INTO Course(title) VALUES('Python');
INSERT INTO Course(title) VALUES('SQL');
INSERT INTO Course(title) VALUES('PHP')
