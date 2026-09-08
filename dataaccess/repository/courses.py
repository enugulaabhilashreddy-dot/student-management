from sqlalchemy.orm import Session
from dataaccess.data_models import Courses, Student, Enrollment
class CourseRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_course(self, course : Courses )-> Courses:
        new_course = Courses(
          
            name = course.name,
            code = course.code,
            max_seats = course.max_seats)

        self.db_session.add(new_course)
        self.db_session.commit()
        self.db_session.refresh(new_course)
        return new_course
    def get_course_by_code(self, code: int):
        return self.db_session.query(Courses).filter(Courses.code == code).first()
    
    def list_courses(self):
        return self.db_session.query(Courses).all()
    
    def get_student_by_id(self, student_id: int):
        return self.db_session.query(Student).filter(Student.id == student_id).first()

    def get_course_by_id(self, course_id: int):
        return self.db_session.query(Courses).filter(Courses.code == course_id).first()
    
    def get_enrollment(self, student_id: int, course_id: int):
        return self.db_session.query(Enrollment).filter(Enrollment.student_id == student_id,Enrollment.course_id == course_id).first()

    def create_enrollment(self, student_id: int, course_id: int):
        enrollment = Enrollment(student_id=student_id,course_id=course_id)

        self.db_session.add(enrollment)
        self.db_session.commit()
        self.db_session.refresh(enrollment)

        return enrollment
    


