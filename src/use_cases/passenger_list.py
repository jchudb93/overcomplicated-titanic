from domain.passenger import Passenger


def passenger_list_use_case(repo):
    return repo.list()


def create_passenger_use_case(repo, passenger: Passenger):
    return repo.create_passenger(passenger)
