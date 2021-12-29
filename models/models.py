from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.sql.expression import null
from db import Base
from datetime import datetime

class Students(Base):
    __tablename__  = "students"
    id             = Column(Integer, primary_key=True, index=True)
    studentID      = Column(Integer, nullable=False)
    fatherName     = Column(String, nullable=False)
    name           = Column(String, nullable=False)
    surname        = Column(String, nullable=False)
    courseID       = Column(Integer, nullable=False)
    facultyID      = Column(Integer, nullable=False)
    klass          = Column(String, nullable=False)
    image          = Column(String, nullable=True)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    
class Parents(Base):
    __tablename__  = "parents"
    id             = Column(Integer, primary_key=True, index=True)
    fatherName     = Column(String, nullable=False)
    name           = Column(String, nullable=False)
    surname        = Column(String, nullable=False)
    birthPlace     = Column(String, nullable=False)
    birthYear      = Column(String, nullable=False)
    yashayanYeri   = Column(String, nullable=False)
    workingPlace   = Column(String, nullable=False)
    sudimost       = Column(String, nullable=False)
    studentID      = Column(Integer, nullable=False)
    parentstatusID = Column(Integer, nullable=False)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    
class studentDetails(Base):
    __tablename__  = "studentDetails"
    id             = Column(Integer, primary_key=True, index=True)
    yashayanYeri   = Column(String, nullable=False)
    okuwaGirenYID  = Column(Integer, nullable=False)
    studentID      = Column(Integer, nullable=False)
    doglanSenesi   = Column(String, nullable=False)
    doglanYeri     = Column(String, nullable=False)
    milleti        = Column(String, nullable=False)
    tamamlanMek    = Column(String, nullable=False)
    bilyanDilleri  = Column(String, nullable=False)
    hunar          = Column(String, nullable=False)
    alymlykDereje  = Column(String, nullable=False)
    bilimi         = Column(String, nullable=False)
    partiyaAgzasy  = Column(String, nullable=False)
    dasYurtBolm    = Column(String, nullable=False)
    mejlisAgzasy   = Column(String, nullable=False)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    
class Faculties(Base):
    __tablename__  = "faculties"
    id             = Column(Integer, primary_key=True, index=True)
    nameTM         = Column(String, nullable=False)
    nameRU         = Column(String, nullable=False)
    nameEN         = Column(String, nullable=False)
    deanID         = Column(Integer)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    
class Welayatlar(Base):
    __tablename__  = "welayatlar"
    id             = Column(Integer, primary_key=True, index=True)
    name           = Column(String, nullable=False)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    
class parentStatus(Base):
    __tablename__  = "parentStatus"
    id             = Column(Integer, primary_key=True, index=True)
    status         = Column(String, nullable=False)
    name           = Column(String, nullable=False)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    
class Registration(Base):
    __tablename__  = "registration"
    id             = Column(Integer, primary_key=True, index=True)
    username       = Column(String, nullable=False)
    password       = Column(String, nullable=False)
    access         = Column(Boolean, nullable=False, default=True)
    staffID        = Column(Integer, nullable=False, default=1)
    token          = Column(String, nullable=False)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)