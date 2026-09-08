from fastapi import APIRouter, HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session

from config.session import get_db
from business_logic.models import CreateCourse
from business_logic.course_logic import Servicelayer
course_router = APIRouter()
# Endpoint 6 - Creating a course

@course_router.post("/courses")
async def create_course(course: CreateCourse, db: Session = Depends(get_db)):
    try:
        service_logic = Servicelayer(db)
        return await service_logic.create_new_course(course)
    except HTTPException:
        raise
    except Exception as e:
        print(f"ERROR: {e}")

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# Endpoint 6b - Listing all courses

@course_router.get("/courses")
def list_all_courses(db: Session = Depends(get_db)):
    try:
        service_logic = Servicelayer(db)
        return service_logic.list_courses()
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(
            status_code=400,
            detail="Unable to get courses" )

# Endpoint 7 - Enrolling student into course

@course_router.post("/students/{student_id}/enroll/{course_id}")
def course_enroll(student_id: int, course_id: int,db: Session = Depends(get_db)):
    try:
        service_logic = Servicelayer(db)
        return service_logic.enroll_student(
            student_id,
            course_id
        )
    except HTTPException:
        raise
    except Exception as e:

        print(f"ERROR: {e}")
        raise HTTPException(
            status_code=400,
            detail="Unable to enroll student"
        )