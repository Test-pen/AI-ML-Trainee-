import csv
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
# Drop old table to apply new constraint
cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT UNIQUE
)
""")

with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?,?)",
                (row["name"], row["email"])
            )
        except sqlite3.IntegrityError:
            print("Duplicate email skipped:", row["email"])

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print({
        "id": row[0],
        "name": row[1],
        "email": row[2]
    })

conn.close()
