import json

from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from repository.memrepo import MemRepo
from use_cases.passenger_list import passenger_list_use_case
from serializers.passenger import PassengerJsonEncoder

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
			"cabin":"C85"
		}
	]
@router.get("/passengers")
async def passenger_list():

	repo = MemRepo(passengers)
	result = passenger_list_use_case(repo)

	content = json.dumps(result, cls=PassengerJsonEncoder)

	headers = {"status_code": "200", "mimetype": "application/json"}
	return JSONResponse(content=content, headers=headers)

