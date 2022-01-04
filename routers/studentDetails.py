from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import studentDetails as studentD, add_studentDetail
from returns import Returns
import json

student_detail_router = APIRouter()


@student_detail_router.post("/add-student-detail")
async def add_student_detail(req: add_studentDetail, db: Session = Depends(get_db)):
    new_add = studentD(**req.dict())
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return Returns.INSERTED
    else:
        return Returns.NOT_INSERTED




@student_detail_router.get("/get-student-detail")
async def get_student_detail(db: Session = Depends(get_db)):
    result = db.query(
        studentD.id,
        studentD.yashayanYeri,
        studentD.salgydakyYeri,
        studentD.okuwaGirenYID,
        studentD.studentID,
        studentD.doglanSenesi,
        studentD.doglanYeri,
        studentD.milleti,
        studentD.tamamlanMek,
        studentD.bilyanDilleri,
        studentD.hunar,
        studentD.alymlykDereje,
        studentD.bilimi,
        studentD.partiyaAgzasy,
        studentD.dasYurtBolm,
        studentD.mejlisAgzasy,
    ).all()
    if not result:
        return Returns.BODY_NULL
    else:
        return result
    
@student_detail_router.put("/update-student-detail")
async def update_student_detail(id: int, req: add_studentDetail, db: Session = Depends(get_db)):
    new_update = db.query(studentD).filter(studentD.id == id).\
        update({
            studentD.yashayanYeri   : req.yashayanYeri,
            studentD.salgydakyYeri  : req.salgydakyYeri,
            studentD.okuwaGirenYID  : req.okuwaGirenYID,
            studentD.studentID      : req.studentID,
            studentD.doglanSenesi   : req.doglanSenesi,
            studentD.doglanYeri     : req.doglanYeri,
            studentD.milleti        : req.milleti,
            studentD.tamamlanMek    : req.tamamlanMek,
            studentD.bilyanDilleri  : req.bilyanDilleri,
            studentD.hunar          : req. hunar,
            studentD.alymlykDereje  : req.alymlykDereje,
            studentD.bilimi         : req.bilimi,
            studentD.partiyaAgzasy  : req.partiyaAgzasy,
            studentD.dasYurtBolm    : req.dasYurtBolm,
            studentD.mejlisAgzasy   : req.mejlisAgzasy,
        }, synchronize_session=False)
    db.commit()
    if new_update:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
    
@student_detail_router.delete("/delete-student-detail")
async def delete_student_detail(id: int, db: Session = Depends(get_db)):
    new_delete = db.query(studentD).filter(studentD.id == id).\
        delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED