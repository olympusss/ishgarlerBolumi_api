from fastapi import FastAPI
from db import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import students_router
from routers import parents_router
from routers import student_detail_router
from routers import faculty_router
from routers import welayat_router
from routers import parent_status_router
from routers import authentication_router
from routers import detail_router
from routers import thirddetails_router

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/uploads', StaticFiles(directory="uploads"), name="uploads")

Base.metadata.create_all(engine)
app.include_router(authentication_router  , tags=["Authentication"])
app.include_router(students_router        , tags=["Students"])
app.include_router(parents_router         , tags=["Parents"])
app.include_router(student_detail_router  , tags=["Student Detail"])
app.include_router(faculty_router         , tags=["Faculty"])
app.include_router(welayat_router         , tags=["Welayat"])
app.include_router(parent_status_router   , tags=["Parent Status"])
app.include_router(detail_router          , tags=["Details"])
app.include_router(thirddetails_router    , tags=["Third Details"])