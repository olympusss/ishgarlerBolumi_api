from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from db import get_db
from models import Parents, add_parent
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