import pytest
import requests


BASE_URL = "http://127.0.0.1:5000/"

def test_get_transaction_info():
    actual_transaction_list = requests.get(f"{BASE_URL}""/Transaction/List")
    assert actual_transaction_list.status_code == 200