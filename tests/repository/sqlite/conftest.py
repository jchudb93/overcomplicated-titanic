import sqlalchemy
import pytest

from src.repository.sqlite.sqlite_objects import Base, Passenger


@pytest.fixture(scope="session")
def sqlite_session_empty():
	conn_str= "sqlite://../titanic.db"
	engine = sqlalchemy.create_engine(conn_str)

	Base.metadata.create_all(engine)
	Base.metadata.bind = engine
	
	DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
	session = DBSession()
	yield session
	session.close()
	connection.close