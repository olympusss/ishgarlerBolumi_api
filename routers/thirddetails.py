from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
from models import (ThirdDetails, IslanYerleri, ThirdDetail_update, ThirdDetail_add,
                    IslanYerleri_add, IslanYerleri_update)

thirddetails_router = APIRouter()

@thirddetails_router.get("/get-third-details")
async def thirddetails(id: int, db: Session = Depends(get_db)):
    result = db.query(
        ThirdDetails.id,
        ThirdDetails.oy_salgysy,
        ThirdDetails.oy_telefony,
        ThirdDetails.el_telefony,
        ThirdDetails.kakasynyn_tel,
        ThirdDetails.ejesinin_tel
    ).filter(ThirdDetails.id == id).all()
    if result:
        return Returns.object(result)
    else:
        return Returns.BODY_NULL
    
    
@thirddetails_router.post("/add-third-details")
async def add_third_details(detail: ThirdDetail_add, db: Session = Depends(get_db)):
    new_add = ThirdDetails(**detail.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return Returns.id(new_add.id)
    else:
        return Returns.NOT_INSERTED
    
    
@thirddetails_router.put("/update-third-details")
async def update_third_details(id: int, req: ThirdDetail_update, db: Session = Depends(get_db)):
    new_update = db.query(ThirdDetails).filter(ThirdDetails.id == id).\
        update({
            ThirdDetails.oy_salgysy    : req.oy_salgysy,
            ThirdDetails.oy_telefony   : req.oy_telefony,
            ThirdDetails.el_telefony   : req.el_telefony,
            ThirdDetails.kakasynyn_tel : req.kakasynyn_tel,
            ThirdDetails.ejesinin_tel  : req.ejesinin_tel
        }, synchronize_session=False)
    db.commit()
    if new_update:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
    
    
@thirddetails_router.delete("/delete-third-details")
async def delete_third_details(id: int, db: Session = Depends(get_db)):
    new_delete = db.query(ThirdDetails).filter(ThirdDetails.id == id).delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED
    
    
@thirddetails_router.get("/get-islan-yerleri")
async def get_islan_yerleri(studentID: int, db: Session = Depends(get_db)):
    result = db.query(
        IslanYerleri.id,
        IslanYerleri.wagt,
        IslanYerleri.yeri
    ).filter(IslanYerleri.studentID == studentID).all()
    if result:
        return Returns.object(result)
    else:
        return Returns.BODY_NULL
    
    
@thirddetails_router.post("/add-islan-yerleri")
async def add_islan_yerleri(req: IslanYerleri_add, db: Session = Depends(get_db)):
    new_add = IslanYerleri(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return Returns.id(new_add.id)
    else:
        return Returns.NOT_INSERTED
    
    
@thirddetails_router.put("/update-islan-yerleri")
async def update_islan_yerleri(id: int, req: IslanYerleri_update, db: Session = Depends(get_db)):
    new_update = db.query(IslanYerleri).filter(IslanYerleri.id == id).\
        update({
            IslanYerleri.wagt : req.wagt,
            IslanYerleri.yeri : req.yeri
        }, synchronize_session=False)
    db.commit()
    if new_update:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
    
    
@thirddetails_router.delete("/delete-islan-yerleri")
async def delete_islan_yerleri(id: int, db: Session = Depends(get_db)):
    new_delete = db.query(IslanYerleri).filter(IslanYerleri.id == id).delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED