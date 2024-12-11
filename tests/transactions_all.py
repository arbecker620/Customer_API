import pytest
import requests




def test_get_transaction_info(client):
    actual_transaction_list = client.get("/Transaction/List")
    assert actual_transaction_list.status_code == 200