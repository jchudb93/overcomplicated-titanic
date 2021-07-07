import json
import pytest

from fastapi import testclient
from src.domain.passenger import Passenger
from src.app import create_app

passenger_dict = [
    {
        "passenger_id": 1,
        "survived": 0,
        "p_class": 3,
        "name": "Braund, Mr. Owen Harris",
        "sex": "male",
        "age": 22,
        "sib_sp": 1,
        "parch": 0,
        "ticket": "A/5 21171",
        "fare": 7.25,
        "cabin": ""
    },
    {
        "passenger_id": 1,
        "survived": 1,
        "p_class": 1,
        "name": "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
        "sex": "female",
        "age": 38,
        "sib_sp": 1,
        "parch": 0,
        "ticket": "PC 17599",
        "fare": 71.2833,
        "cabin": "C85"
    }
]

@pytest.fixture
def client():
	app, settings = create_app()
	client = testclient.TestClient(app)
	return client

def test_get(client):
	http_response = client.get("/passengers")
	assert json.loads(http_response.json()) == passenger_dict
	assert http_response.status_code == 200