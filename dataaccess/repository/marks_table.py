from sqlalchemy.orm import Session
from dataaccess.data_models import Student, marks


class MarksRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session
    # Get student
    def get_student_by_id(self, student_id: int):

        return self.db_session.query(Student).filter(Student.id == student_id).first()

    
    def create_marks(self, new_marks):

        self.db_session.add(new_marks)
        self.db_session.commit()
        self.db_session.refresh(new_marks)

        return new_marks

   
    def get_marks_by_student(self, student_id: int):
        return self.db_session.query(marks).filter(marks.student_id == student_id).all()