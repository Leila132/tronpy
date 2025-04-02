from repositories.query_repository import QueryRepository
from schemas.address import Address
from models.query import Query
from services.tron_api import TronApiClient
from typing import List


class QueryService:
    def __init__(self, repository: QueryRepository):
        self.repository = repository
        self.tron_client = TronApiClient()

    def create_query(self, query: Address) -> Query:
        data = self.tron_client.get_tron_data(address=query)
        return self.repository.create(data)

    def get_queries(self) -> List:
        return self.repository.get_all()
