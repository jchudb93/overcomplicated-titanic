import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from domain.passenger import Passenger
from log import REQUEST_LOGGER
from repository.firestore_repository.passenger_repository import FirestoreRepository
from repository.memrepo import MemRepo
from serializers.passenger import PassengerJsonEncoder
from use_cases.passenger_list import passenger_list_use_case, create_passenger_use_case
from pydantic import BaseModel

router = APIRouter()

passengers = [
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


class CreatePassengerModel(BaseModel):
    passenger_id: int
    name: str
    sex: str
    age: int


@router.get("/passengers")
async def passenger_list():
    REQUEST_LOGGER.info('Request: /passengers')
    repo = MemRepo(passengers)
    result = passenger_list_use_case(repo)

    content = json.dumps(result, cls=PassengerJsonEncoder)

    headers = {"status_code": "200", "mimetype": "application/json"}
    return JSONResponse(content=content, headers=headers)


@router.post("/passengers/")
async def create_passenger(passenger: CreatePassengerModel):
    repo = FirestoreRepository()
    result = create_passenger_use_case(repo, passenger)

    content = json.dumps(result)
    headers = {"status_code": "201", "mimetype": "application/json"}
    return JSONResponse(content=content, headers=headers)
