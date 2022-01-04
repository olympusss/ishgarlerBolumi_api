from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
from models import detail_schema, Details as D


detail_router = APIRouter()

@detail_router.get("/get-detail")
async def get_detail(db: Session = Depends(get_db)):
    result = db.query(
        D.id,
        D.salgydaky_yeri,
        D.jynsy,
        D.harby_gulluk,
        D.UYJ_galyarmy,
        D.UYJ_otag_belgi,
        D.passport_belgi,
        D.passport_berlen_senesi,
        D.passport_kim_tar_berl,
        D.masgala_yagdayy,
        D.onki_familiyasy,
        D.wel_bol_UYJ_cykanlar
    ).all()
    if result:
        return Returns.object(result)
    else:
        return Returns.BODY_NULL
    
    
@detail_router.post("/add-detail")
async def add_detail(detail: detail_schema, db: Session = Depends(get_db)):
    new_add = D(**detail.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return Returns.INSERTED
    else:
        return Returns.NOT_INSERTED
    
    
@detail_router.put("/update-detail")
async def update_detail(id: int, req: detail_schema, db: Session = Depends(get_db)):
    new_update = db.query(D).filter(D.id == id).\
        update({
            D.salgydaky_yeri         : req.salgydaky_yeri,
            D.jynsy                  : req.jynsy,
            D.harby_gulluk           : req.harby_gulluk,
            D.UYJ_galyarmy           : req.UYJ_galyarmy,
            D.UYJ_otag_belgi         : req.UYJ_otag_belgi,
            D.passport_belgi         : req.passport_belgi,
            D.passport_berlen_senesi : req.passport_berlen_senesi,
            D.passport_kim_tar_berl  : req.passport_kim_tar_berl,
            D.masgala_yagdayy        : req.masgala_yagdayy,
            D.onki_familiyasy        : req.onki_familiyasy,
            D.wel_bol_UYJ_cykanlar   : req.wel_bol_UYJ_cykanlar
        }, synchronize_session=False)
    db.commit()
    if new_update:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
    
    
@detail_router.delete("/delete-detail")
async def delete_detail(id: int, db: Session = Depends(get_db)):
    new_delete = db.query(D).filter(D.id == id).\
        delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED