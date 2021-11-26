from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from db import get_db
from models import Students, add_student
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