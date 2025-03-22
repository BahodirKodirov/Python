Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.

Populate your new table with the following values:

Name	Species	Age
Benjamin Sisko	Human	40
Jadzia Dax	Trill	300
Kira Nerys	Bajoran	29
Update the Name of Jadzia Dax to be Ezri Dax

Display the Name and Age of everyone in the table classified as Bajoran.

import sqlite3

# Step 1: Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('starfleet.db')
cursor = conn.cursor()

# Step 2: Create the Roster table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
''')

# Step 3: Insert initial data into the Roster table
cursor.executemany('''
    INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
''', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# Commit the changes
conn.commit()

# Step 4: Update the Name of Jadzia Dax to Ezri Dax
cursor.execute('''
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
''')

# Commit the changes
conn.commit()

# Step 5: Query for Bajoran species and display Name and Age
cursor.execute('''
    SELECT Name, Age
    FROM Roster
    WHERE Species = 'Bajoran'
''')

bajoran_results = cursor.fetchall()

# Display the results
print("Bajoran Roster:")
for row in bajoran_results:
    print(f"Name: {row[0]}, Age: {row[1]}")

# Step 6: Close the connection
conn.close()

