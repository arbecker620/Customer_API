import pytest
import requests

# Base URL for the API (replace with your actual API endpoint)
BASE_URL = "http://127.0.0.1:5000/"

# Helper function to make GET requests to the API
# Test cases
def test_get_home_page():
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200

def test_home_redirect(client):
    response = requests.get(f"{BASE_URL}")
    assert len(response.history)==1
    assert response.request.path  == "/home"


    # Verify that the actual list matches the expected list
    #assert isinstance(actual_customers_list, list)
    
