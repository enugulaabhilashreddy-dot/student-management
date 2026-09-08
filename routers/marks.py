from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from config.session import get_db
from business_logic.models import AddMarks
from business_logic.marks_logic import MarksService


marks_router = APIRouter()


# Endpoint 8 - Add marks

@marks_router.post("/students/{student_id}/marks")
def add_marks(student_id: int, marks_data: AddMarks, db: Session = Depends(get_db)):
    try:
        service_logic = MarksService(db)
        return service_logic.add_marks(
            student_id,
            marks_data.subject_name,
            marks_data.marks
        )
    except HTTPException:
        raise
    except Exception as e:

        print(f"ERROR: {e}")

        raise HTTPException(
            status_code=400,
            detail="Unable to add marks"
        )
# Endpoint 9 - Get result

@marks_router.get("/students/{student_id}/result")
def get_result(student_id: int,db: Session = Depends(get_db)):
    try:
        service_logic = MarksService(db)

        return service_logic.get_result(student_id)

    except HTTPException:
        raise
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(
            status_code=400,
            detail="Unable to get result"
        )