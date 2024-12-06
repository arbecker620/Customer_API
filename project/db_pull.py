import sqlite3

def get_db_connection(table):

    conn = sqlite3.connect(table)
    conn.row_factory = sqlite3.Row
    return conn




conn = get_db_connection('Customer.db')
cur = conn.cursor()
    
    # Execute a query to retrieve all APi calls
cur.execute('SELECT * FROM Transactions')
    
    # Fetch all rows from the executed query
rows = cur.fetchall()
    
    # Convert rows to a list of dictionaries
transactions = [dict(row) for row in rows]
    
    # Close the database connection
conn.close()

print(transactions)