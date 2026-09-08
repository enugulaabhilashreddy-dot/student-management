from sqlalchemy import  Column,  Integer, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Student(Base):
    __tablename__ = "StudentTable"
    id = Column(Integer,primary_key=True,index = True)
    name = Column(String, index = True)
    email = Column(String, index = True)
    department = Column(String, default = "CSE")
    year  = Column(Integer)
    is_deleted = Column(default = False)

class Courses(Base):
    __tablename__ = "CourseTable"
    name = Column(String, index = True)
    code = Column(Integer, primary_key = True, index =True)
    max_seats = Column(Integer)
    
class Enrollment(Base):
    __tablename__ = "EnrollmentTable"

    enrollment_id = Column(Integer,primary_key=True,index=True)
    student_id = Column(Integer,ForeignKey("StudentTable.id"))
    course_id = Column(Integer,ForeignKey("CourseTable.code"))
    is_deleted = Column(default=False)

class marks(Base):
    __tablename__ = "MarksScored"
    marks_id = Column(Integer, primary_key=True,index=True)
    student_id = Column(Integer,ForeignKey("StudentTable.id"))
    subject_name = Column(String)
    marks = Column(Integer)
    is_deleted = Column(default=False)

    