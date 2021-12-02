from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy.sql.operators import endswith_op
from db import get_db
from models import Parents, add_parent, update_parent
from returns import Returns

parents_router = APIRouter()

@parents_router.post("/add-parent")
def add_parent(req: add_parent, db: Session = Depends(get_db)):
    new_add = Parents(
        fatherName     = req.fatherName,
        name           = req.name,
        surname        = req.surname,
        birthPlace     = req.birthPlace,
        birthYear      = req.birthYear,
        yashayanYeri   = req.yashayanYeri,
        workingPlace   = req.workingPlace,
        sudimost       = req.sudimost,
        studentID      = req.studentID,
        parentstatusID = req.parentstatusID
    )
    
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return Returns.INSERTED
    else:
        return Returns.NOT_INSERTED
    
@parents_router.get("/get-parent")
def get_parent(db: Session = Depends(get_db)):
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
    ).all()
    if result:
        return result
    else:
        return Returns.BODY_NULL
    
    
@parents_router.put("/update-parent")
def update_parent(id: int, req: update_parent, db: Session = Depends(get_db)):
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
            Parents.studentID       : req.studentID,
            Parents.parentstatusID  : req.parentstatusID
        }, synchronize_session=False)
    db.commit()
    if new_update:
        return Returns.UPDATED
    else:   
        return Returns.NOT_UPDATED
    
@parents_router.delete("/delete-parent")
def delete_parent(id: int, db: Session = Depends(get_db)):
    new_delete = db.query(Parents).filter(Parents.id == id).\
        delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED