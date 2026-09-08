from fastapi import HTTPException
from sqlalchemy.orm import Session

from business_logic.models import CreateCourse
from dataaccess.data_models import Courses
from dataaccess.repository.courses import CourseRepository


class Servicelayer:

    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.course_repo = CourseRepository(self.db_session)

    # Endpoint 6 - Creating a course
    async def create_new_course(self, course: CreateCourse):

        existing = self.course_repo.get_course_by_code(course.code)

        if existing is not None:
            raise HTTPException(
                status_code=400,
                detail="A course with this code already exists"
            )

        new_course = Courses(
            name=course.name,
            code=course.code,
            max_seats=course.max_seats
        )

        db_result = self.course_repo.create_course(new_course)

        return {
            "message": "Course created successfully"
        }

    # Endpoint 6b - Listing all courses
    def list_courses(self):

        return self.course_repo.list_courses()

    # Endpoint 7 - Enrolling student into course
    def enroll_student(self, student_id: int, course_id: int):

        student = self.course_repo.get_student_by_id(student_id)

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        course = self.course_repo.get_course_by_id(course_id)

        if course is None:
            raise HTTPException(
                status_code=404,
                detail="Course not found"
            )

        existing_enrollment = self.course_repo.get_enrollment(
            student_id,
            course_id
        )

        if existing_enrollment is not None:
            raise HTTPException(
                status_code=400,
                detail="Already enrolled in this course"
            )

        self.course_repo.create_enrollment(
            student_id,
            course_id
        )

        return {
            "message": "Student enrolled successfully"
        }