from fastapi import FastAPI

from app.database.database import create_db_and_tables
from app.api.v1.router import router as v1_router

app = FastAPI(
    title="Dispatcher"
)


@app.on_event("startup")
def init_db():
    create_db_and_tables()


app.include_router(v1_router)
