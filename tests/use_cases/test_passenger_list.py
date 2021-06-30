import pytest

from unittest import mock

from src.domain.passenger import Passenger
from src.use_cases.passenger_list import passenger_list_use_case


@pytest.fixture
def domain_passengers():
	passenger1 = Passenger(
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

	passenger2 = Passenger(
		passenger_id=1,
		survived=1,
		p_class=1,
		name="Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
		sex="female",
		age=38,
		sib_sp=1,
		parch=0,
		ticket="PC 17599",
		fare=71.2833,
		cabin="C85"
	)

	return [passenger1, passenger2]

def test_passenger_without_parameters(domain_passengers):
	repo = mock.Mock()
	repo.list.return_value = domain_passengers

	result = passenger_list_use_case(repo)

	repo.list.assert_called_with()
	assert result == domain_passengers