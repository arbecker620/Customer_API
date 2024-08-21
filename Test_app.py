import pytest
import requests

# Base URL for the API (replace with your actual API endpoint)
BASE_URL = "http://127.0.0.1:5000/"

# Helper function to make GET requests to the API
# Test cases
def test_get_home_page():
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200

def test_get_customer_info_valid_id():
    route_test = "Customer"
    customer_id = 'AA001'  # Example of a valid customer ID



    expected_customers_list = [
    {"id": 1, "name": "John Doe", "address": '122 Blueberry Ln','Date_of_Birth':'6/20/1990', 'Customer_ID':'AA001'},
    {"id": 2, "name": "Jane Smith", "address": '221 Strawberry St','Date_of_Birth':'6/20/1995','Customer_ID':'AA002'},
    {"id": 3, "name": "Alice Johnson", "address": '212 Orange Ct','Date_of_Birth': '7/20/2000','Customer_ID':'AA003'},
    ]
    actual_customers_list = requests.get(f"{BASE_URL}""/Customers/List")
    assert actual_customers_list.status_code == 200
    # Verify that the actual list matches the expected list
    #assert isinstance(actual_customers_list, list)
    
