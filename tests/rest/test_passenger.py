import json
from unittest import mock

from src.domain.passenger import Passenger

passenger_dict = {
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
		}

passengers = [Passenger.from_dict(passenger_dict)]

@mock.patch("src.rest.passenger.passenger_list_use_case")
def test_get(mock_use_case, client):
	mock_use_case.return_value = passengers
	http_response = client.get("/pasengers")

	assert json.loads(http_response.data.decode("UTF-8")) == [passenger_dict]
	mock_use_case.assert_called()
	assert http_response.status_code == 200
	assert http_response.mimetype == "application/json"