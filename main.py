from fastapi import FastAPI

from routers.student import student_router
from routers.course import course_router
from routers.marks import marks_router
app = FastAPI(title="student management system")

app.include_router(student_router)
app.include_router(course_router)
app.include_router(marks_router)