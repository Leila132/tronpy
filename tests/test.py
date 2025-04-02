from repositories.query_repository import QueryRepository
from models.query import Query


# integration tests
def test_get_enpoint(test_client):
    payment_url = "/tronpy_manager/"
    response = test_client.get(payment_url)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_successful_post_enpoint(test_client):
    payment_url = "/tronpy_manager/"
    data = {"address": "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL"}
    response = test_client.post(payment_url, json=data)
    assert response.status_code == 200
    payment_url = "/tronpy_manager/"
    response = test_client.get(payment_url)
    assert len(response.json()) == 2


def test_fail_post_enpoint(test_client):
    payment_url = "/tronpy_manager/"
    data = {"not_address": "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL"}
    response = test_client.post(payment_url, json=data)
    assert response.status_code == 422
    data = {"address": 100}
    response = test_client.post(payment_url, json=data)
    assert response.status_code == 422


# unit tests
def test_add_info_to_bd(db_with_test_data, query_data):
    repo = QueryRepository(db_with_test_data)
    result = repo.create(query_data)
    assert result.id is not None
    assert db_with_test_data.query(Query).count() == 2
    assert result.address == query_data["address"]
