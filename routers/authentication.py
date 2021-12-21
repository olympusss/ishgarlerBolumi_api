from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
from models import authentication, Registration
from tokens import create_access_token

authentication_router = APIRouter()

@authentication_router.post("/authentication")
def authentication(req: authentication, db: Session = Depends(get_db)):
    token_dict = {
        "username" : req.username,
        "password" : req.password
    }
    token = create_access_token(data=token_dict)
    token_res = {"token" : token}
    new_add = Registration(
        username = req.username,
        password = req.password,
        token    = token
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return Returns.object(token_res)
    else:
        return Returns.NOT_INSERTED