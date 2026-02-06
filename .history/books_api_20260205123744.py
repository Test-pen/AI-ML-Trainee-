import requests
import sqlite3

# Step 1: Call API
url = "https://openlibrary.org/subjects/love.json?limit=5"
response = requests.get(url)
data = response.json()

# Step 2: Create Database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
year INTEGER
)
""")

# Step 3: Insert Data
for book in data["works"]:
    title = book["title"]

    if "authors" in book:
        author = book["authors"][0]["name"]
    else:
        author = "Unknown"

    year = book.get("first_publish_year", 0)

    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?,?,?)",
        (title, author, year)
    )

conn.commit()

# Step 4: Display Data
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
