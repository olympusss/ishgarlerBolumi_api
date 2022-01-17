from fastapi import APIRouter, Depends, Request, UploadFile, File
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, and_, or_
from db import get_db
from models import Students, add_student, update_student, Details, ThirdDetails, studentDetails
from returns import Returns
import sys
import os
import shutil
import uuid

students_router = APIRouter()

@students_router.post("/add-student")
async def add_student(req: add_student, db: Session = Depends(get_db)):
    new_add = Students(**req.dict())
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return Returns.id(new_add.id)
    else:
        return Returns.NOT_INSERTED
    
@students_router.get("/get-student")
async def get_student(id: int, db: Session = Depends(get_db)):
    result = db.query(
        Students.id,
        Students.studentID,
        Students.fatherName,
        Students.name,
        Students.surname,
        Students.courseID,
        Students.facultyID,
        Students.klass,
        Students.image
    ).filter(Students.id == id).first()
    if result:
        return Returns.object(result)
    else:
        return Returns.BODY_NULL
    
@students_router.post("/get-students")
async def get_student(page: int, db: Session = Depends(get_db)):
    result = db.query(
        Students.id,
        Students.studentID,
        Students.fatherName,
        Students.name,
        Students.surname,
        Students.courseID,
        Students.facultyID,
        Students.klass,
        Students.image,
        Details.tayyatlyk_ugry,
        ThirdDetails.el_telefony,
        studentDetails.id.label("student_detail_id"),
        Details.id.label("detail_id"),
        ThirdDetails.id.label("third_detail_id")
    )
    result_count = result.count()
    result = result.join(Details, Details.studentID == Students.id)
    result = result.join(ThirdDetails, ThirdDetails.student_id == Students.id)
    result = result.join(studentDetails, studentDetails.studentID == Students.id)
    result = result.order_by(desc(Students.createAt)).offset(30 * (page - 1)).limit(30).all()
    final_result = {}
    final_result["students"] = result
    final_result["count"] = (result_count // 30) + 1
    if final_result:
        return Returns.object(final_result)
    else:
        return Returns.BODY_NULL
    
@students_router.put("/update-student")
async def update_student(id: int, req: update_student, db: Session = Depends(get_db)):
    new_update = db.query(Students).filter(Students.id == id).\
        update({
            Students.fatherName : req.fatherName,
            Students.name       : req.name,
            Students.surname    : req.surname,
            Students.courseID   : req.courseID,
            Students.facultyID  : req.facultyID,
            Students.klass      : req.klass
        }, synchronize_session=False)
    db.commit()
    if new_update:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
    
@students_router.delete("/delete-student")
async def delete_student(id: int, db: Session = Depends(get_db)):
    new_delete = db.query(Students).filter(Students.id == id).\
        delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED
    
@students_router.put("/upload-image")
async def upload_image(id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    sp = file.filename.split(".")
    extension = sp[-1]
    random = str(uuid.uuid4())
    new_name = random + "." + extension
    
    path = sys.path[0] + "/uploads/students/"
    if not os.path.exists(path):
        os.makedirs(path)
    path = path + f"{new_name}"
    upload_file_path = "uploads/students/" + new_name

    
    with open(path,  "wb") as file_object:
        shutil.copyfileobj(file.file, file_object)
        
    new_update = db.query(Students).filter(Students.id == id).\
        update({Students.image: upload_file_path}, synchronize_session=False)
    db.commit()
    if new_update:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED