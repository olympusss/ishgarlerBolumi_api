from fastapi import FastAPI
from db import Base, engine
from routers import students_router
from routers import parents_router

app = FastAPI()
Base.metadata.create_all(engine)

app.include_router(students_router, tags=["Students"])
app.include_router(parents_router,  tags=["Parents"])