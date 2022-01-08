from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import parentStatus
from returns import Returns
import json

parent_status_router = APIRouter()

@parent_status_router.get("/get-parent-status")
async def get_parent_status(db: Session = Depends(get_db)):
    result = db.query(
        parentStatus.id,
        parentStatus.name
    ).all()
    if result:
       return Returns.object(result)
    
    f = open("json/parent_status.json")
    data = json.load(f)
    for i in data:
        name_json = i.get("name")
        new_add = parentStatus(
            name = name_json
        )
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        if not new_add:
            return Returns.NOT_INSERTED
    f.close()
    result = db.query(
        parentStatus.id,
        parentStatus.name
    ).all()
    if result:
        return Returns.object(result)
    else:
        return Returns.BODY_NULL