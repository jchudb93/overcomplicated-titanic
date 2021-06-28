import uuid
from src.domain.passenger import Passenger 


def test_passenger_model_init():
	code = uuid.uuid4
	passenger = Passenger(
		code = code,
		passenger_id = 1,
		survived = 0,
		name = "Braund, Mr. Owen Harris",
		sex = "male",
		age = 22,
		sib_sp = 0,
		parch = 0,
		ticket = "A/5 21171",
		fare = 7.25,
		cabin = ""
	)

	assert passenger.code == code
	assert passenger.passenger_id == 1
	assert passenger.survived == 0
	assert passenger.name == "Braund, Mr. Owen Harris"
	assert passenger.sex == "male"
	assert passenger.age == 22
	assert passenger.sib_sp == 0
	assert passenger.parch == 0
	assert passenger.ticket == "A/5 21171"
	assert passenger.fare == 7.25
	assert passenger.cabin == ""