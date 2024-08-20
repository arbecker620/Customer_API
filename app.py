from flask import Flask, request, jsonify, make_response
import sqlite3
# Create a Flask app
app = Flask(__name__)
from os import environ



def get_db_connection():
    conn = sqlite3.connect('passengers.db')
    conn.row_factory = sqlite3.Row
    return conn



# Define a route and its corresponding function
@app.route('/home')
def hello():
    return 'Hello, World!'


@app.route('/passengers', methods = ['GET'])
def get_passengers():
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Execute a query to retrieve all passengers
    cur.execute('SELECT * FROM passengers')
    
    # Fetch all rows from the executed query
    rows = cur.fetchall()
    
    # Convert rows to a list of dictionaries
    passengers = [dict(row) for row in rows]
    
    # Close the database connection
    conn.close()
    
    return jsonify(passengers)

@app.route('/passenger/<int:id>', methods=['GET'])
def get_passenger(id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Execute a query to retrieve a specific passenger by ID
    cur.execute('SELECT * FROM passengers WHERE id = ?', (passenger_id,))
    
    # Fetch one row from the executed query
    row = cur.fetchone()
    
    # Close the database connection
    conn.close()
    
    if row is None:
        return jsonify({"error": "Passenger not found"}), 404
    
    # Convert the row to a dictionary
    passenger = dict(row)
    
    return jsonify(passenger)



# Run the app if this script is executed directly
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=4000)