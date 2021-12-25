from fastapi import APIRouter, Depends, Request, UploadFile, File
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, and_, or_
from db import get_db
from models import Students, add_student, update_student, filter_students
from returns import Returns
import sys
import os
import shutil

students_router = APIRouter()

@students_router.post("/add-student")
def add_student(req: add_student, db: Session = Depends(get_db)):
    new_add = Students(
        studentID  = req.studentID,
        fatherName = req.fatherName,
        name       = req.name,
        surname    = req.surname,
        courseID   = req.courseID,
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
        Students.courseID,
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
            Students.courseID   : req.course,
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
    
@students_router.put("/upload-image")
def upload_image(id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    
    path = sys.path[0] + "uploads\students"
    if not os.path.exists(path):
        os.makedirs(path)
    path = path + f"\\{file.filename}"
    upload_file_path = "uploads/students/" + file.filename
    
    with open(path,  "wb") as file_object:
        shutil.copyfileobj(file.file, file_object)
        
    new_update = db.query(Students).filter(Students.id == id).\
        update({Students.image: upload_file_path}, synchronize_session=False)
    db.commit()
    if new_update:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
        
    