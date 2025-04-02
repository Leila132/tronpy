from sqlalchemy.orm import Session
from models.query import Query
from typing import List


class QueryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, query_data: dict) -> Query:
        db_query = Query(**query_data)
        self.db.add(db_query)
        self.db.commit()
        self.db.refresh(db_query)
        return db_query

    def get_all(self) -> List:
        return self.db.query(Query).all()
