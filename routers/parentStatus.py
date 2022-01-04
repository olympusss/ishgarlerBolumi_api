from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import parentStatus
from returns import Returns

parent_status_router = APIRouter()

@parent_status_router.get("/get-parent-status")
async def get_parent_status(db: Session = Depends(get_db)):
    result = db.query(
        parentStatus.id,
        parentStatus.name,
        parentStatus.status,
    ).all()
    if not result:
        return Returns.BODY_NULL
    else:
        return result