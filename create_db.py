import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("movie.db")
cursor = conn.cursor()

# Create movies table with rating column
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating REAL DEFAULT 0.0
)
""")

# Insert sample movies with ratings
cursor.executemany("""
INSERT INTO movies (title, genre, rating) VALUES (?, ?, ?)
""", [
    ("The Shawshank Redemption", "Drama", 9.3),
    ("The Dark Knight", "Action", 9.0),
    ("Inception", "Sci-Fi", 8.8),
    ("Forrest Gump", "Drama", 8.8),
    ("The Matrix", "Sci-Fi", 8.7),
    ("Pulp Fiction", "Crime", 8.9),
    ("Gladiator", "Action", 8.5),
    ("Titanic", "Romance", 7.8),
('The Godfather', 'Crime', 9.2),
('Schindler''s List', 'Drama', 8.9),
('Inception', 'Sci-Fi', 8.8),
('Fight Club', 'Drama', 8.8),
('Forrest Gump', 'Drama', 8.8),
('The Matrix', 'Sci-Fi', 8.7),
('The Lord of the Rings: The Return of the King', 'Fantasy', 8.9),
('The Empire Strikes Back', 'Sci-Fi', 8.7),
('Interstellar', 'Sci-Fi', 8.6),
('The Green Mile', 'Drama', 8.6),
('The Lion King', 'Animation', 8.5),
('Avengers: Endgame', 'Action', 8.4),
('Saving Private Ryan', 'War', 8.6),
('The Silence of the Lambs', 'Thriller', 8.6),
('Parasite', 'Thriller', 8.5),
('Whiplash', 'Drama', 8.5),
('Django Unchained', 'Western', 8.4),
('WALL-E', 'Animation', 8.4),
('The Prestige', 'Drama', 8.5),
('The Departed', 'Crime', 8.5),
('Joker', 'Drama', 8.4),
('The Wolf of Wall Street', 'Biography', 8.2),
('Mad Max: Fury Road', 'Action', 8.1),
('Black Panther', 'Action', 7.3),
('Toy Story', 'Animation', 8.3)
    
])

conn.commit()
conn.close()

print("Database created and populated successfully with ratings!")
