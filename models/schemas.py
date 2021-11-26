from pydantic import BaseModel

from db.connection import Base

class add_student(BaseModel):
    studentID   : str
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