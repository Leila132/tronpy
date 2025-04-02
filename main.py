from fastapi import FastAPI
from routers import queries
from config.database import engine, Base

app = FastAPI()
app.include_router(queries.router)

Base.metadata.create_all(bind=engine)
