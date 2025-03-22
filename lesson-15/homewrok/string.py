Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.

Populate your new table with the following values:

Name	Species	Age
Benjamin Sisko	Human	40
Jadzia Dax	Trill	300
Kira Nerys	Bajoran	29
Update the Name of Jadzia Dax to be Ezri Dax

Display the Name and Age of everyone in the table classified as Bajoran.
-- SQLite:
sqlite3 mydatabase.db

-- MySQL:
CREATE DATABASE mydatabase;
USE mydatabase;

-- PostgreSQL:
CREATE DATABASE mydatabase;
\c mydatabase;

-- Create the Roster table
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);

-- Insert data into the Roster table
INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);

-- Update the Name of Jadzia Dax to Ezri Dax
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';

-- Display the Name and Age of everyone classified as Bajoran
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran';
