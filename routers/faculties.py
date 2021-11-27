from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Faculties
from returns import Returns


faculty_router = APIRouter()

@faculty_router.get("/get-faculty")
def get_faculty(db: Session = Depends(get_db)):
    result =  db.query(
        Faculties.id,
        Faculties.nameTM,
        Faculties.nameRU,
        Faculties.nameEN,
        Faculties.deanID,
    ).all()
    if not result:
        return Returns.BODY_NULL
    else:
        return result