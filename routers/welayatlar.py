from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Welayatlar
from returns import Returns
import json

welayat_router = APIRouter()

@welayat_router.get("/get-welayat")
def get_welayat(db: Session = Depends(get_db)):
    result = db.query(
        Welayatlar.id,
        Welayatlar.name,
    ).all()
    
    if result:
        return Returns.object(result)
    f = open('json/welayatlar.json')
    data = json.load(f)
    for i in data:
        name_json: str = i.get('name')
        new_add = Welayatlar(name = name_json)
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        if not new_add:
            return Returns.NOT_INSERTED
    result = db.query(
        Welayatlar.id,
        Welayatlar.name,
    ).all()
    if result:
        return Returns.object(result)
    else:
        return Returns.BODY_NULL