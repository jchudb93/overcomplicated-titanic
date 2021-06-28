import dataclasses

@dataclasses.dataclass
class Passenger:
	passenger_id: int
	survived: int
	p_class: int
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