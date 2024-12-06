import pytest
import requests

# Base URL for the API (replace with your actual API endpoint)


# Helper function to make GET requests to the API
# Test cases
def test_get_home_page(client):
    response = client.get("/home")
    assert response.status_code == 200

def test_home_redirect(client):
    response = client.get("/home")
    assert response.request.path  == "/home"


    # Verify that the actual list matches the expected list
    #assert isinstance(actual_customers_list, list)
    
