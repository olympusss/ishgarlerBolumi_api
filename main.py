from fastapi import FastAPI
from db import Base, engine
from routers import students_router
from routers import parents_router
from routers import student_detail_router
from routers import faculty_router
from routers import welayat_router
from routers import parent_status_router

app = FastAPI()
Base.metadata.create_all(engine)

app.include_router(students_router,       tags=["Students"])
app.include_router(parents_router,        tags=["Parents"])
app.include_router(student_detail_router, tags=["Student Detail"])
app.include_router(faculty_router,        tags=["Faculty"])
app.include_router(welayat_router,        tags=["Welayat"])
app.include_router(parent_status_router,  tags=["Parent Status"])