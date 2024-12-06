import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Customer.db')

# Create a cursor object
cur = conn.cursor()

# Create passengers table
cur.execute('''
CREATE TABLE IF NOT EXISTS Customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    Date_of_Birth TEXT NOT NULL,
    Customer_ID TEXT NOT NULL
)
''')
 
# Insert some sample data
cur.executemany('''
INSERT INTO Customer (name, address, Date_of_Birth, Customer_ID)
VALUES (?, ?, ?, ?)
''', [
    ('John Doe', '122 Blueberry Ln', '6/20/1990', 'bc349b6a-a176-11ef-91be-0242ac110002'),
    ('Jane Smith', '221 Strawberry St', '6/20/1995','bc34a042-a176-11ef-91be-0242ac110002'),
    ('Alice Johnson', '212 Orange Ct', '7/20/2000', 'bc34a1a0-a176-11ef-91be-0242ac110002')
])
cur.execute('''
CREATE TABLE IF NOT EXISTS Transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    route TEXT
)'''
)
conn.commit()
conn.close()



