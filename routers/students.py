from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
from db import get_db
from models import Students, add_student, update_student
from returns import Returns

students_router = APIRouter()

@students_router.post("/add-student")
def add_student(req: add_student, db: Session = Depends(get_db)):
    new_add = Students(
        studentID  = req.studentID,
        fatherName = req.fatherName,
        name       = req.name,
        surname    = req.surname,
        course     = req.course,
        facultyID  = req.facultyID,
        klass      = req.klass
    )
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return Returns.INSERTED
    else:
        return Returns.NOT_INSERTED
    
@students_router.get("/get-student")
def get_student(db: Session = Depends(get_db)):
    result = db.query(
        Students.id,
        Students.studentID,
        Students.fatherName,
        Students.name,
        Students.surname,
        Students.course,
        Students.facultyID,
        Students.klass
    ).all()
    if result:
        return result
    else:
        return Returns.BODY_NULL
    
@students_router.put("/update-student")
def update_student(id: int, req: update_student, db: Session = Depends(get_db)):
    new_update = db.query(Students).filter(Students.id == id).\
        update({
            Students.studentID  : req.studentID,
            Students.fatherName : req.fatherName,
            Students.name       : req.name,
            Students.surname    : req.surname,
            Students.course     : req.course,
            Students.facultyID  : req.facultyID,
            Students.klass      : req.klass
        }, synchronize_session=False)
    db.commit()
    if new_update:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
    
@students_router.delete("/delete-student")
def delete_student(id: int, db: Session = Depends(get_db)):
    new_delete = db.query(Students).filter(Students.id == id).\
        delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED