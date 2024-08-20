import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('passengers.db')

# Create a cursor object
cur = conn.cursor()

# Create passengers table
cur.execute('''
CREATE TABLE IF NOT EXISTS passengers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    flight_number TEXT NOT NULL,
    seat_number TEXT NOT NULL
)
''')

# Insert some sample data
cur.executemany('''
INSERT INTO passengers (name, flight_number, seat_number)
VALUES (?, ?, ?)
''', [
    ('John Doe', 'AA123', '12A'),
    ('Jane Smith', 'BA456', '14C'),
    ('Alice Johnson', 'CA789', '18B')
])

# Commit the changes and close the connection
conn.commit()
conn.close()