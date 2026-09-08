from sqlalchemy.orm import Session
from data_models import Enrollment
class StudentRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_enrollment(self, enroll : Enrollment )-> Enrollment:
        new_enrollment = Enrollment(
            enrollment_id = enroll.enrollment_id,
            student_id = enroll.student_id,
            course_id = enroll.course_id)

        self.db_session.add(new_enrollment)
        self.db_session.commit(new_enrollment)
        self.db_session.refresh(new_enrollment)
        return new_enrollment
