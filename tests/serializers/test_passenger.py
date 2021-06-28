import json

from src.serializers.passenger import PassengerJsonEncoder
from src.domain.passenger import Passenger

def test_serialize_domain_passenger():


	passenger = Passenger(
		passenger_id=1,
		survived=0,
		p_class=3,
		name="Braund, Mr. Owen Harris",
		sex="male",
		age=22,
		sib_sp=1,
		parch=0,
		ticket="A/5 21171",
		fare=7.25,
		cabin=""
	)

	expected_json = f"""
		{{
			"passenger_id": 1,
			"survived": 0,
			"p_class": 3,
			"name": "Braund, Mr. Owen Harris",
			"sex":"male",
			"age": 22,
			"sib_sp": 1,
			"parch": 0,
			"ticket": "A/5 21171",
			"fare": 7.25,
			"cabin": ""	
		}}
	"""

	json_passenger = json.dumps(passenger, cls=PassengerJsonEncoder)
	assert json.loads(json_passenger) == json.loads(expected_json)