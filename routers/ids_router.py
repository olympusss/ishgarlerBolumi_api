from ast import Return
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Details, studentDetails, ThirdDetails
from returns import Returns

ids_router = APIRouter()

@ids_router.get("/all-ids")
async def get_ids(db: Session = Depends(get_db)):
    details = db.query(Details.id).all()
    student_details = db.query(studentDetails.id).all()
    third_details = db.query(ThirdDetails.id).all()
    result = {}
    result["details_ids"] = details
    result["student_details_ids"] = student_details
    result["third_details_ids"] = third_details
    return Returns.object(result)