
from fastapi import APIRouter
from sqlalchemy.orm import Session
# from app.MODELS.db_conn import get_db
# from app.MODELS import db_user 
from fastapi import Depends
router = APIRouter()

@router.get("/users")
def get_users():
    return {"message": "List of users"}