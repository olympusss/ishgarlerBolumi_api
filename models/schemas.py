from pydantic import BaseModel

from db.connection import Base

class add_student(BaseModel):
    studentID   : int
    fatherName  : str
    name        : str
    surname     : str
    course      : str
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
    course      : str
    facultyID   : int
    klass       : str
    
    class Config:
        orm_mode = True