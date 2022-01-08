from pydantic import BaseModel
from typing import List
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
    salgydakyYeri  : str
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
    parentstatusID : int
    
    class Config:
        orm_mode = True   

class update_student(BaseModel):
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
        
class detail_schema(BaseModel):
    salgydaky_yeri         : str
    jynsy                  : int
    harby_gulluk           : int
    UYJ_galyarmy           : int
    UYJ_otag_belgi         : str
    passport_belgi         : str
    passport_berlen_senesi : str
    passport_kim_tar_berl  : str
    masgala_yagdayy        : int
    onki_familiyasy        : str
    wel_bol_UYJ_cykanlar   : int
    
    class Config:
        orm_mode = True
        
        
class ThirdDetail_update(BaseModel):
    oy_salgysy    : str
    oy_telefony   : str
    el_telefony   : str
    kakasynyn_tel : str
    ejesinin_tel  : str
    
    class Config:
        orm_mode = True
        
class ThirdDetail_add(ThirdDetail_update):
    studentD_id   : int
    
    class Config:
        orm_mode = True
        
    
class IslanYerleri_update(BaseModel):
    wagt : str
    yeri : str
    
    class Config:
        orm_mode = True
        
class IslanYerleri_add(IslanYerleri_update):
    studentID : int
    
    class Config:
        orm_mode = True