from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql+psycopg2://postgres:1425@127.0.0.1:5432/clinic_backend"#COlocar nome do banco

engine = create_engine(DATABASE_URL, echo = False, future = True)

SessionLocal = sessionmaker (bind = engine, autoflush = False, autocommit = False, future = True)

def get_session():
    return SessionLocal()

class Base(DeclarativeBase):
    pass