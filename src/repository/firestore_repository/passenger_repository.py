from domain.passenger import Passenger
from repository.firestore_repository.connection import get_firestore_client


class FirestoreRepository:

    def __init__(self):
        pass

    def create_passenger(self, passenger: Passenger):
        with get_firestore_client() as firestore_client:
            doc_ref = firestore_client.collection(u'users').document(passenger.name)
            doc_ref.set({
                'passenger_id': passenger.passenger_id,
                'name': passenger.name,
                'age': passenger.age,
                'sex': passenger.sex,
            })
