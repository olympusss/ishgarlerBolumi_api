from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from sqlalchemy import and_, or_
from models import Parents, add_parent, update_parent
from returns import Returns
from typing import Optional


parents_router = APIRouter()

@parents_router.post("/add-parent")
async def add_parent(req: add_parent, db: Session = Depends(get_db)):
    new_add = Parents(**req.dict())
    
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return Returns.id(new_add.id)
    else:
        return Returns.NOT_INSERTED
    
@parents_router.get("/get-parent")
async def get_parent(studentID: int, db: Session = Depends(get_db)):
    result = db.query(
        Parents.id,
        Parents.fatherName,
        Parents.name,
        Parents.surname,
        Parents.birthPlace,
        Parents.birthYear,
        Parents.yashayanYeri,
        Parents.workingPlace,
        Parents.sudimost,
        Parents.studentID,
        Parents.parentstatusID
    ).filter(Parents.studentID == studentID).all()
    if result:
        return Returns.object(result)
    else:
        return Returns.BODY_NULL
    
    
@parents_router.put("/update-parent")
async def update_parent(id: int, req: update_parent, db: Session = Depends(get_db)):
    new_update = db.query(Parents).filter(Parents.id == id).\
        update({
            Parents.fatherName      : req.fatherName,
            Parents.name            : req.name,
            Parents.surname         : req.surname,
            Parents.birthPlace      : req.birthPlace,
            Parents.birthYear       : req.birthYear,
            Parents.yashayanYeri    : req.yashayanYeri,
            Parents.workingPlace    : req.workingPlace,
            Parents.sudimost        : req.sudimost,
            Parents.parentstatusID  : req.parentstatusID
        }, synchronize_session=False)
    db.commit()
    if new_update:
        return Returns.UPDATED
    else:   
        return Returns.NOT_UPDATED
    
@parents_router.delete("/delete-parent")
async def delete_parent(id: Optional[int] = None, studentID: Optional[int] = None, db: Session = Depends(get_db)):
    new_delete = db.query(Parents).filter(or_(Parents.id == id, Parents.studentID == studentID)).\
        delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED