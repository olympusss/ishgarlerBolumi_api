from pydantic import BaseModel
from typing import List

from sqlalchemy.sql.expression import true
from db.connection import Base

class add_student(BaseModel):
    studentID   : int
    fatherName  : str
    name        : str
    surname     : str
    courseID    : int
    facultyID   : int
    klass       : str
    
    class Config:
        orm_mode = True
        
class add_parent(BaseModel):
    fatherName     : str
    name           : str
    surname        : str
    birthPlace     : str
    birthYear      : str
    yashayanYeri   : str
    workingPlace   : str
    sudimost       : str
    studentID      : int
    parentstatusID : int
    
    class Config:
        orm_mode = True
        
class add_studentDetail(BaseModel):
    yashayanYeri   : str
    okuwaGirenYID  : int
    studentID      : int
    doglanSenesi   : str
    doglanYeri     : str
    milleti        : str
    tamamlanMek    : str
    bilyanDilleri  : str
    hunar          : str
    alymlykDereje  : str
    bilimi         : str
    partiyaAgzasy  : str
    dasYurtBolm    : str
    mejlisAgzasy   : str
    
    class Config:
        orm_mode = True
    
class update_parent(BaseModel):
    fatherName     : str
    name           : str
    surname        : str
    birthPlace     : str
    birthYear      : str
    yashayanYeri   : str
    workingPlace   : str
    sudimost       : str
    studentID      : int
    parentstatusID : int
    
    class Config:
        orm_mode = True   

class update_student(BaseModel):
    studentID   : int
    fatherName  : str
    name        : str
    surname     : str
    courseID    : int
    facultyID   : int
    klass       : str
    
    class Config:
        orm_mode = True
        
class filter_students(BaseModel):
    filterField : List[str] = []
    filterValue : List = []
    sort        : str
    sortType    : int
    limit       : int
    page        : int
    
    class Config:
        orm_mode = True
    
    
class sign_in(BaseModel):
    username    : str
    password    : str
    
    class Config:
        orm_mode = True
            
class sign_up(sign_in):
    access      : bool
    staffID     : int
    class Config:
        orm_mode = True