from src.domain.passenger import Passenger

class MemRepo:
	def __init__(self, data):
		self.data = data

	def list(self):
		return [Passenger.from_dict(i) for i in self.data]