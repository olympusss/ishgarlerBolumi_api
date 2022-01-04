from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from db import get_db
from sqlalchemy import and_, or_
from returns import Returns
from models import sign_up, Registration, sign_in
from tokens import create_access_token, check_token

authentication_router = APIRouter()

@authentication_router.post("/sign-up")
async def log_on(req: sign_up, db: Session = Depends(get_db)):
    get_user = db.query(
        Registration.username,
        Registration.password
    ).filter(
        and_(
            Registration.username == req.username, 
            Registration.password == req.password
        )).first()
    if get_user:
        return Returns.BODY_NULL
    token_dict = {
        "username" : req.username,
        "password" : req.password
    }
    token = create_access_token(data=token_dict)
    token_res = {"token" : token}
    new_add = Registration(
        **req.dict(), 
        token = token
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return Returns.object(token_res)
    else:
        return Returns.NOT_INSERTED
    
@authentication_router.post("/sign-in")
async def sign_in(req: sign_in, db: Session = Depends(get_db)):
    get_user = db.query(Registration.token).\
        filter(and_(
            Registration.username == req.username,
            Registration.password == req.password,
        )).first()
    if not get_user:
        return Returns.BODY_NULL
    else:
        return Returns.object(get_user)