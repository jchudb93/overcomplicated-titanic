from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Passenger(Base):
	__tablename__ = "passenger"
	passenger_id = Column(Integer)
	survived = Column(Integer)
	p_class = Column(Integer)
	name = Column(String(100))
	sex = Column(String(20))
	age = Column(Integer)
	sib_sip = Column(Integer)
	parch = Column(Integer)
	ticket = Column(String(100))
	fare = Column(Float)
	cabin = Column(String(100))