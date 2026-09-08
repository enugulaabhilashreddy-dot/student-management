from pydantic import BaseModel
class StudentCreate(BaseModel):
    id : int
    name : str
    email : str
    department : str = "CSE"
    year: int

    @classmethod
    def from_db(cls, db_details):
        return cls(
            id=db_details.id,
            name=db_details.name,
            email=db_details.email,
            department=db_details.department,
            year=db_details.year
        )
class CreateCourse(BaseModel):
    name : str
    code : int
    max_seats :int

    @classmethod
    def from_db(cls, db_details):
        return cls(
            name = db_details.name,
            code = db_details.code,
            max_seats = db_details.max_seats
        )

class AddMarks(BaseModel):
    subject_name: str
    marks: int