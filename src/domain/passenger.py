import uuid
import dataclasses

@dataclasses.dataclass
class Passenger:
	code: uuid.UUID
	passenger_id: int
	survived: int
	name: str
	sex: str
	age: int
	sib_sp: int
	parch: int
	ticket: str
	fare: float
	cabin: str

	@classmethod
	def from_dict(self, d):
		return self(**d)

	def to_dict(self):
		return dataclasses.asdict(self)