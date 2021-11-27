from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Welayatlar
from returns import Returns

welayat_router = APIRouter()

@welayat_router.get("/get-welayat")
def get_welayat(db: Session = Depends(get_db)):
    result = db.query(
        Welayatlar.id,
        Welayatlar.name,
    ).all()
    if not result:
        return Returns.BODY_NULL
    else:
        return result