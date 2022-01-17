from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from db import Base
from sqlalchemy.orm import relationship
from datetime import datetime



class Students(Base):
    __tablename__  = "students"
    id             = Column(Integer, primary_key=True, index=True)
    studentID      = Column(Integer, nullable=False)
    fatherName     = Column(String, nullable=False)
    name           = Column(String, nullable=False)
    surname        = Column(String, nullable=False)
    courseID       = Column(Integer, ForeignKey("courses.id"))
    facultyID      = Column(Integer, ForeignKey("faculties.id"))
    klass          = Column(String, nullable=False)
    image          = Column(String, nullable=True)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    students_parents        = relationship("Parents"       , back_populates="parents_students")
    students_studentdetails = relationship("studentDetails", back_populates="studentdetails_students")
    students_faculties      = relationship("Faculties"     , back_populates="faculties_students")
    students_courses        = relationship("Courses"       , back_populates="courses_students")
    students_islanyerleri   = relationship("IslanYerleri"  , back_populates="islanyerleri_students")
    students_details        = relationship("Details"       , back_populates="details_students")
    students_thirddetails   = relationship("ThirdDetails"  , back_populates="thirddetails_students")
    
    
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
    studentID      = Column(Integer, ForeignKey("students.id"))
    parentstatusID = Column(Integer, ForeignKey("parentStatus.id"))
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    parents_students     = relationship("Students", back_populates="students_parents")
    parents_parentstatus = relationship("parentStatus", back_populates="parentstatus_parents")
    
class studentDetails(Base):
    __tablename__  = "studentDetails"
    id             = Column(Integer, primary_key=True, index=True)
    yashayanYeri   = Column(String, nullable=False)
    salgydakyYeri  = Column(String, nullable=False)
    okuwaGirenYID  = Column(Integer, ForeignKey("welayatlar.id"))
    studentID      = Column(Integer, ForeignKey("students.id"))
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
    studentdetails_students     = relationship("Students"    , back_populates="students_studentdetails")
    studentdetails_welayatlar   = relationship("Welayatlar"  , back_populates="welayatlar_studentdetails")
    
class Faculties(Base):
    __tablename__  = "faculties"
    id             = Column(Integer, primary_key=True, index=True)
    nameTM         = Column(String, nullable=False)
    nameRU         = Column(String, nullable=False)
    nameEN         = Column(String, nullable=False)
    deanID         = Column(Integer)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    faculties_students = relationship("Students", back_populates="students_faculties")
    
class Welayatlar(Base):
    __tablename__  = "welayatlar"
    id             = Column(Integer, primary_key=True, index=True)
    name           = Column(String, nullable=False)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    welayatlar_studentdetails = relationship("studentDetails", back_populates="studentdetails_welayatlar")
    
class parentStatus(Base):
    __tablename__  = "parentStatus"
    id             = Column(Integer, primary_key=True, index=True)
    name           = Column(String, nullable=False)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    parentstatus_parents = relationship("Parents", back_populates="parents_parentstatus")
    
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
    
class Details(Base):
    __tablename__          = "details"
    id                     = Column(Integer, primary_key=True, index=True)
    salgydaky_yeri         = Column(String,  nullable=False, default='Lebap')
    studentID              = Column(Integer, ForeignKey("students.id"))
    temmi                  = Column(String,  nullable=True)
    jynsy                  = Column(Integer, nullable=False, default=1)
    harby_gulluk           = Column(Integer, nullable=False, default=0)
    UYJ_galyarmy           = Column(Integer, nullable=False, default=1)
    UYJ_otag_belgi         = Column(String,  nullable=True)
    passport_belgi         = Column(String,  nullable=False)
    passport_berlen_senesi = Column(String,  nullable=False)
    passport_kim_tar_berl  = Column(String,  nullable=False)
    masgala_yagdayy        = Column(Integer, nullable=False, default=0)
    onki_familiyasy        = Column(String,  nullable=True)
    wel_bol_UYJ_cykanlar   = Column(Integer, nullable=False, default=1)
    tayyatlyk_ugry         = Column(String,  nullable=False)
    bellik                 = Column(String,  nullable=True)
    createAt               = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt               = Column(DateTime, default=datetime.now(), nullable=False)
    details_students       = relationship("Students", back_populates="students_details")
    
class Courses(Base):
    __tablename__  = "courses"
    id             = Column(Integer, primary_key=True, index=True)
    name           = Column(String, nullable=False)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    courses_students = relationship("Students", back_populates="students_courses")
    

class IslanYerleri(Base):
    __tablename__  = "islan_yerleri"
    id             = Column(Integer, primary_key=True, index=True)
    wagt           = Column(String,  nullable=False, default="123456789")
    yeri           = Column(String, nullable=False, default="Lebap Energo")
    studentID      = Column(Integer, ForeignKey("students.id"))
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    islanyerleri_students = relationship("Students", back_populates="students_islanyerleri")
    

class ThirdDetails(Base):
    __tablename__  = "third_details"
    id             = Column(Integer, primary_key=True, index=True)
    oy_salgysy     = Column(String,  nullable=False, default="123456789")
    oy_telefony    = Column(String,  nullable=False, default="123456789")
    el_telefony    = Column(String,  nullable=False, default="123456789")
    kakasynyn_tel  = Column(String,  nullable=False, default="123456789")
    ejesinin_tel   = Column(String,  nullable=False, default="123456789")
    student_id    = Column(Integer, ForeignKey("students.id"), default=2)
    createAt       = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt       = Column(DateTime, default=datetime.now(), nullable=False)
    thirddetails_students = relationship("Students", back_populates="students_thirddetails")