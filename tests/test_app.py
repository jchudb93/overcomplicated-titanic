import pytest


from fastapi import testclient
from src.app import create_app

@pytest.fixture
def app():
	app, settings = create_app()
	client = testclient.TestClient(app)
	response = client.get("/")
	assert settings.app_name == "Titanic API"
	assert response.status_code == 200
	assert response.json() == {"msg": "Hello World"}