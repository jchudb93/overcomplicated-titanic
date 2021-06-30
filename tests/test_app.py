import pytest

from src.app import create_app

@pytest.fixture
def app():
	app, settings = create_app()

	return app, settings