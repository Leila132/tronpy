from sqlalchemy import Column, Integer, String, Float
from config.database import Base


class Query(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    balance = Column(Float)
    bandwidth = Column(Integer)
    energy = Column(Integer)
