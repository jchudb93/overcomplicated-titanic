import uuid
from src.domain.passenger import Passenger 


def test_passenger_model_init():

	init_dict = {
		"code": uuid.uuid4,
		"passenger_id": 1,
		"survived": 0,
		"name": "Braund, Mr. Owen Harris",
		"sex": "male",
		"age": 22,
		"sib_sp": 0,
		"parch": 0,
		"ticket": "A/5 21171",
		"fare": 7.25,
		"cabin": ""
	}

	passenger = Passenger.from_dict(init_dict)

	assert passenger.to_dict() == init_dict