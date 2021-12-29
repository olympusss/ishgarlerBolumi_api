from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Faculties
from returns import Returns
import json


faculty_router = APIRouter()

@faculty_router.get("/get-faculty")
def get_faculty(db: Session = Depends(get_db)):
    result =  db.query(
        Faculties.id,
        Faculties.nameTM.label("name")
    ).all()
    if result:
        return Returns.object(result)
    f = open("json/fakultetler.json")
    data = json.load(f)
    for i in data:
        name_json = i.get("name")
        new_add = Faculties(
            nameTM = name_json,
            nameRU = name_json,
            nameEN = name_json
        )
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        if not new_add:
            return Returns.NOT_INSERTED
    f.close()
    result =  db.query(
        Faculties.id,
        Faculties.nameTM.label("name")
    ).all()
    if result:
        return Returns.object(result)
    else:
        return Returns.BODY_NULL