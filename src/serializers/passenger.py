import json

class PassengerJsonEncoder(json.JSONEncoder):
	def default(self, o):
		try:
			to_serialize = {
				"passenger_id": o.passenger_id,
				"survived": o.survived,
				"p_class": o.p_class,
				"name": str(o.name),
				"sex": str(o.sex),
				"age": o.age,
				"sib_sp": o.sib_sp,
				"parch": o.parch,
				"ticket": str(o.ticket),
				"fare": o.fare,
				"cabin": str(o.cabin)
			}
			return to_serialize
		except AttributeError: # pragma: no cover
			return super().default(o)