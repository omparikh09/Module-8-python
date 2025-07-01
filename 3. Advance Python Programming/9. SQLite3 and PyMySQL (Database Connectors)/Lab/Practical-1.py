"""
Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.
"""

import sqlite3

# Connect to (or create) a database
conn = sqlite3.connect("example.db")  
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

# Commit the changes
conn.commit()

# Fetch and display all data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()