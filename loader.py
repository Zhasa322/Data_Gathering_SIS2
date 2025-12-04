import sqlite3
import json




#Create the database
conn = sqlite3.connect("data/movie_database.db")
cursor = conn.cursor()

#Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id TEXT PRIMARY KEY,
    title TEXT,
    year INTEGER,
    rating INTEGER
)
""")

#Load the file in read mode
with open("data/cleaned_movies.json", "r") as f:
    movies = json.load(f)

#Insert the data into table
for movie in movies:
    cursor.execute("""
    INSERT OR REPLACE INTO movies (id, title, year, rating)
    VALUES (?, ?, ?, ?)
    """, (
        movie.get("id"),
        movie.get("title"),
        movie.get("year"),
        movie.get("rating")
    ))



#Save the changes and close connection
conn.commit()
conn.close()
