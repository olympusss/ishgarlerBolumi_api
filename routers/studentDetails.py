from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import studentDetails as studentD, add_studentDetail
from returns import Returns

student_detail_router = APIRouter()


@student_detail_router.post("/add-student-detail")
def add_student_detail(req: add_studentDetail, db: Session = Depends(get_db)):
    new_add = studentD(
        yashayanYeri    = req.yashayanYeri,
        okuwaGirenYID   = req.okuwaGirenYID,
        studentID       = req.studentID,
        doglanSenesi    = req.doglanSenesi,
        doglanYeri      = req.doglanYeri,
        milleti         = req.milleti,
        tamamlanMek     = req.tamamlanMek,
        bilyanDilleri   = req.bilyanDilleri,
        hunar           = req.hunar,
        alymlykDereje   = req.alymlykDereje,
        bilimi          = req.bilimi,
        partiyaAgzasy   = req.partiyaAgzasy,
        dasYurtBolm     = req.dasYurtBolm,
        mejlisAgzasy    = req.mejlisAgzasy
    )
    if new_add:
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        return Returns.INSERTED
    else:
        return Returns.NOT_INSERTED




@student_detail_router.get("/get-student-detail")
def get_student_detail(db: Session = Depends(get_db)):
    result = db.query(
        studentD.id,
        studentD.yashayanYeri,
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