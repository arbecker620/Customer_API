import pytest
import requests




def test_get_customer_info_valid_id(client):
    route_test = "Customer"
    customer_id = 'AA001'  # Example of a valid customer ID



    expected_customers_list = [
    {"id": 1, "name": "John Doe", "address": '122 Blueberry Ln','Date_of_Birth':'6/20/1990', 'Customer_ID':'AA001'},
    {"id": 2, "name": "Jane Smith", "address": '221 Strawberry St','Date_of_Birth':'6/20/1995','Customer_ID':'AA002'},
    {"id": 3, "name": "Alice Johnson", "address": '212 Orange Ct','Date_of_Birth': '7/20/2000','Customer_ID':'AA003'},
    ]
    actual_customers_list = client.get("/Customers/List")
    assert actual_customers_list.status_code == 200