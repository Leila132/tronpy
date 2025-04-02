from pydantic import BaseModel


class QueryBase(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int


class QueryCreate(QueryBase):
    pass


class Query(QueryBase):
    id: int

    class Config:
        from_attributes = True
