from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from db import Base
from datetime import datetime

class Students(Base):
    __tablename__  = "students"
    id             = Column(Integer, primary_key=True, index=True)
    studentID      = Column(String, nullable=False)
    fatherName     = Column(String, nullable=False)
    name           = Column(String, nullable=False)
    surname        = Column(String, nullable=False)
    course         = Column(String, nullable=False)
    facultyID      = Column(Integer, nullable=False)
    klass          = Column(String, nullable=False)
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