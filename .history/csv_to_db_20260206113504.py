import csv
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT
)
""")

# Clear old data
cursor.execute("DELETE FROM users")

with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?,?)",
            (row["name"], row["email"])
        )

conn.commit()

# Fetch data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print in JSON-like format
for row in rows:
    print({
        "id": row[0],
        "name": row[1],
        "email": row[2]
    })

conn.close()
