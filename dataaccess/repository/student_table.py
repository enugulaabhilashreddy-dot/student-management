from sqlalchemy.orm import Session
from dataaccess.data_models import Student
class StudentRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_student(self, student : Student )-> Student:
        new_student = Student(
            id = student.id,
            name = student.name,
            email = student.email,
            department = student.department,
            year = student.year)

        self.db_session.add(new_student)
        self.db_session.commit()
        self.db_session.refresh(new_student)
        return new_student
    
    def list_students(self):
        return self.db_session.query(Student).filter(Student.is_deleted == False).all()
    
    def get_student_by_id(self, student_id: int):
        return self.db_session.query(Student).filter(Student.id == student_id,Student.is_deleted == False).first()
    
    def update_student(self, student: Student):
        self.db_session.commit()
        self.db_session.refresh(student)
        return student
    
    def remove_a_student(self, id :int):
        student = self.db_session.query(Student).filter(Student.id == id).first()
        if student is None:
            return None
        student.is_deleted = True
        self.db_session.add(student)
        self.db_session.commit()
        return True
    
