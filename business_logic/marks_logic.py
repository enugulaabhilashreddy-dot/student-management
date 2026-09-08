from fastapi import HTTPException
from sqlalchemy.orm import Session

from business_logic.models import AddMarks
from dataaccess.data_models import marks
from dataaccess.repository.marks_table import MarksRepository


class MarksService:

    def __init__(self, db_session: Session):

        self.db_session = db_session
        self.marks_repo = MarksRepository(self.db_session)

    # Endpoint 8 - Add marks
    def add_marks(
        self,
        student_id: int,
        subject_name: str,
        student_marks: int
    ):

        student = self.marks_repo.get_student_by_id(student_id)

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        if student_marks < 0 or student_marks > 100:
            raise HTTPException(
                status_code=400,
                detail="Marks must be between 0 and 100"
            )

        new_marks = marks(
            student_id=student_id,
            subject_name=subject_name,
            marks=student_marks
        )

        self.marks_repo.create_marks(new_marks)

        return {
            "message": "marks added successfully"
        }

    # Endpoint 9 - Get result
    def get_result(self, student_id: int):

        student = self.marks_repo.get_student_by_id(student_id)

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        get_marks = self.marks_repo.get_marks_by_student(student_id)

        if not get_marks:

            return {
                "student_id": student_id,
                "marks": [],
                "average": None,
                "result": "no marks recorded"
            }

        average = sum(
            mark.marks for mark in get_marks
        ) / len(get_marks)

        if average >= 40:
            result = "pass"
        else:
            result = "fail"

        return {
            "student_id": student_id,
            "marks": [
                {
                    "subject": mark.subject_name,
                    "marks": mark.marks
                }
                for mark in get_marks
            ],
            "average": average,
            "result": result
        }