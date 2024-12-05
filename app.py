from flask import Flask, request, jsonify, make_response, redirect, g
import sqlite3
# Create a Flask app
app = Flask(__name__)


from os import environ
import time
from flask_caching import Cache
import redis
import uuid
#from blueprints.Customers import Customer



#app.register_blueprint()
cache = redis.Redis(host='redis', port=6379)

def get_db_connection(table):

    conn = sqlite3.connect(table)
    conn.row_factory = sqlite3.Row
    return conn
 

"""
def create_app():
    app = Flask(__name__)
    app.config['CACHE_TYPE'] = 'redis'
    app.config['CACHE_REDIS_HOST'] = 'localhost'
    app.config['CACHE_REDIS_PORT'] = 6379
    app.config['CACHE_REDIS_DB'] = 0
    # Initialize Flask-Caching with Redis
    cache = Cache(app=app)
    cache.init_app(app)
    # Initialize Redis client
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    app.run(debug=True)
"""



@app.before_request
def log_route_start():
    g.start_time = time.time()
    
@app.after_request
def log_route_end(response):
    route = request.endpoint
    conn = get_db_connection('Customer.db')
    
    print(f"{route} ended after {time.time() - g.pop('start_time', None)}")
    
    conn = sqlite3.connect('Customer.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Transactions(route) VALUES(?)''', (route,))
    conn.commit()
    conn.close()
    return response



# Define a route and its corresponding function
@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/')
def redirect_home():
    return redirect('/home')

@app.route('/Customers/List', methods = ['GET'])
def get_customers_list():


    conn = get_db_connection('Customer.db')
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


@app.route('/Transaction/List', methods = ['GET'])
def get_transactions_list():
    
    conn = get_db_connection('Customer.db')
    cur = conn.cursor()
    
    # Execute a query to retrieve all APi calls
    cur.execute('SELECT * FROM Transactions')
    
    # Fetch all rows from the executed query
    rows = cur.fetchall()
    print(rows)
    if rows is None:
        return jsonify({"error": "No Transactions"}), 404
    
    # Convert rows to a list of dictionaries
    transactions = [dict(row) for row in rows]
    
    # Close the database connection
    conn.close()
    
    return jsonify(transactions)

@app.route('/Customer/<string:id>', methods=['GET'])
def get_customer(id):
    conn = get_db_connection('Customer.db')
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

@app.route('/Customer/', methods = ['POST'])
def create_customer():
    data = request.get_json()
    #name, address, Date_of_Birth, Customer_ID
    name = data.get('Name')
    address = data.get('address')
    dob = data.get('Date_of_Birth')

    if not name or not address or not dob:
        return jsonify({'error': 'name address and DPB are required'}), 409

    conn = get_db_connection('Customer.db')
    cur = conn.cursor()
    customerid = str(uuid.uuid1())

    cur.execute('''INSERT INTO Customer (name, address, Date_of_Birth, Customer_ID)
        VALUES (?, ?, ?, ?)
            ''', (name, address, dob, customer_id))
    conn.commit()
    conn.close()
    return jsonify({'Status': 'Customer Added'}), 200


# Run the app if this script is executed directly
if __name__ == '__main__':
	#app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
    #create_app()