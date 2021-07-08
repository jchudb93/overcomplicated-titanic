from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Passenger(Base):
	__tablename__ = "passenger"
	passenger_id = Column(Integer)
	