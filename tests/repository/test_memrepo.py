import pytest

from src.domain.passenger import Passenger
from src.repository.memrepo import MemRepo

@pytest.fixture
def passenger_dict():
	return [
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


def test_repository_list_without_parameters(passenger_dict):
	repo = MemRepo(passenger_dict)
	passengers = [Passenger.from_dict(i) for i in passenger_dict]
	assert repo.list() == passengers