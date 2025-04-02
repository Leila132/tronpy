from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from config.database import Base, get_db
from main import app
from fastapi.testclient import TestClient
from models.query import Query

config = dotenv_values()

SQL_DB_URL = config["SQL_TEST_DB_URL"]

engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Create a new database session with a rollback at the end of the test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def db_with_test_data(db_session):
    db_session.query(Query).delete()
    db_session.commit()

    test_messages = [
        Query(address="TestAddress", balance=220.84, bandwidth=100, energy=100),
    ]
    db_session.add_all(test_messages)
    db_session.commit()

    yield db_session


@pytest.fixture(scope="function")
def test_client(db_with_test_data):
    def override_get_db():
        try:
            yield db_with_test_data
        finally:
            db_with_test_data.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def query_data():
    """Generate a query data."""
    return {
        "address": "Testaddress",
        "balance": 220.84,
        "bandwidth": 100,
        "energy": 100,
    }
