from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv

import os

load_dotenv()

connection_string = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('POSTGRES_DB')}"

engine = create_engine(connection_string, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_database():
    with Session(engine) as session:
        yield session
