# noinspection PyUnresolvedReferences
from tests.test_app import app


def test_serialize_domain_passenger(app):
    client = app
    response = client.get("/passengers")
    assert response.status_code == 200
