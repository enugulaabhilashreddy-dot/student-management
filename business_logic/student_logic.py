from sqlalchemy.orm import Session
from business_logic.models import StudentCreate,CreateCourse
from dataaccess.data_models import Student
from dataaccess.repository.student_table import StudentRepository 
class Servicelayer:
    def __init__(self, db_session:Session):
        self.db_session = db_session
        self.student_repo = StudentRepository(self.db_session)
        self.get_student = StudentRepository(self.db_session)
        

    async def create_new_student(self, Create_student: StudentCreate):

        try:
            print(f"request {Create_student}")
            create_new_student = Student(
                id = Create_student.id,
                name = Create_student.name,
                email = Create_student.email,
                department = Create_student.department,
                year = Create_student.year
                )
            
            db_result = self.student_repo.create_student(create_new_student)
            print("check")
            print(f"DB result is {StudentCreate.from_db(db_result)}")
            return StudentCreate.from_db(db_result)
        except Exception as e:
            print(f"{e}")
            print(f"Unable to create")
    def list_students(self):
        return self.db_session.query(Student).all()
    
    def get_student_by_id(self, student_id : int):
        return self.db_session.query(Student).filter(Student.id == student_id).first()
    
    def update_student_details(self, student_id :int,student:StudentCreate):
        existing_student= (self.db_session.query(Student).filter( Student.id == student_id).first())
        if existing_student is None:
            return None
        
        existing_student.id = student.id ,   
        existing_student.name = student.name,
        existing_student.email = student.email,
        existing_student.department = student.department,
        existing_student.year = student.year
        return existing_student
    def remove_a_student(self, student_id:int):
        try:
            db_result = self.student_repo.remove_a_student(student_id)
            if db_result is None:
                return None
            return{"message": "student details deleted successfully"}
        except Exception as e:
            print(f"Error as {e}")

            print(f"can't find student with id {student_id}")

   

      





