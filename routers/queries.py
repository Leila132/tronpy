from fastapi import APIRouter, Depends
from services.query_service import QueryService
from repositories.query_repository import QueryRepository
from schemas.query import QueryCreate
from schemas.address import Address
from config.database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix="/tronpy_manager", tags=["Queries"])


@router.post("/", response_model=QueryCreate)
async def create_query(query: Address, db: Session = Depends(get_db)):
    repository = QueryRepository(db)
    service = QueryService(repository)
    return service.create_query(query)


@router.get("/", response_model=List[QueryCreate])
async def get_queries(db: Session = Depends(get_db)):
    repository = QueryRepository(db)
    service = QueryService(repository)
    return service.get_queries()
