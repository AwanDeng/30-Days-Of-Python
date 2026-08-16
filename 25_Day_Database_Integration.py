# Day 25 - Database operations using SQLite

import sqlite3

# Connect to an in-memory database
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# 1. Create a table
cursor.execute("CREATE TABLE users (id INT, name TEXT, role TEXT)")

# 2. Insert records
cursor.execute("INSERT INTO users VALUES (1, 'Alex', 'Developer')")
cursor.execute("INSERT INTO users VALUES (2, 'Sarah', 'Analyst')")
connection.commit()

# 3. Query records
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()