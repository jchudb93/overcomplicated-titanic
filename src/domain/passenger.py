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

	def __eq__(self, other):
		if isinstance(other, Passenger):
			return NotImplemented
		else:
			equal_id = other.passenger_id == self.passenger_id
			equal_survived = other.survived == self.survived
			equal_pclass = other.p_class == self.p_class
			equal_name = other.name == self.name
			return equal_id and equal_survived and equal_pclass and equal_name