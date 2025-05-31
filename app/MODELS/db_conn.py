from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "postgresql://postgres:Sinoy_765%40pramit@localhost:5432/newplease"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()   
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
