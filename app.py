from flask import Flask, request, jsonify, make_response, redirect
import sqlite3
# Create a Flask app
app = Flask(__name__)
from os import environ



def get_db_connection():
    conn = sqlite3.connect('Customer.db')
    conn.row_factory = sqlite3.Row
    return conn



# Define a route and its corresponding function
@app.route('/home')
def hello():
    return 'Hello, World!'

@app.route('/')
def home():
    return redirect('/home')



@app.route('/Customers/List', methods = ['GET'])
def get_customers():
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Execute a query to retrieve all passengers
    cur.execute('SELECT * FROM Customer')
    
    # Fetch all rows from the executed query
    rows = cur.fetchall()
    
    # Convert rows to a list of dictionaries
    customers = [dict(row) for row in rows]
    
    # Close the database connection
    conn.close()
    
    return jsonify(customers)

@app.route('/Customer/<int:id>', methods=['GET'])
def get_customer(id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Execute a query to retrieve a specific passenger by ID
    cur.execute('SELECT * FROM Customer WHERE id = ?', (id,))
    
    # Fetch one row from the executed query
    row = cur.fetchone()
    
    # Close the database connection
    conn.close()
    
    if row is None:
        return jsonify({"error": "Customer not found"}), 404
    
    # Convert the row to a dictionary
    customer = dict(row)
    
    return jsonify(customer)



# Run the app if this script is executed directly
if __name__ == '__main__':
	app.run(debug=True)