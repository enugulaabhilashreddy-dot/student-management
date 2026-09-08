from pydantic import BaseModel,Field
class StudentCreate(BaseModel):
    id : int
    name : str
    email : str
    department : str = "CSE"
    year: int

class course_created(BaseModel):
    name : str
    code : int
    max_seats : int

class student_enroll(BaseModel):
    enrollment_id : int
    student_id : int
    course : int
    
class AddMarks(BaseModel):
    subject_name: str
    marks: int


