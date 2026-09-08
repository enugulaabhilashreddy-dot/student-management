from fastapi import APIRouter, HTTPException, Depends
from routers.models import StudentCreate, course_created
from sqlalchemy.orm import Session
from config.session import get_db
from business_logic.student_logic import Servicelayer

student_router = APIRouter()

# POST - Create Task
@student_router.post("/")
async def add_student(AddStudent: StudentCreate, db: Session = Depends(get_db)):
    print("hey")
    try:
        service_logic = Servicelayer(db_session=db)
        service_response = await service_logic.create_new_student(AddStudent)
        return StudentCreate.model_dump(service_response)
    except Exception as e:
        print(f"Not working as expected {e}")
        raise HTTPException(detail="Unable to create student at the moment", status_code=400)

@student_router.get("/students")
def get_students(db: Session = Depends(get_db)):
    print("this is is one")
    try:
        service_logic = Servicelayer(db_session=db)       
        service_response = service_logic.list_students()      
        return service_response
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(
            detail="Unable to get students at the moment",
            status_code=400
        )
    
@student_router.get("/students/{student_id}")
def get_student(student_id : int,db:Session = Depends(get_db)):
    try :
        service_logic = Servicelayer(db_session =db)
        service_response = service_logic.get_student_by_id(student_id)
        return service_response
    except Exception as e:
        print("ERROR", e)
        raise HTTPException(
            detail = "could not find the student ID", status_code = 400
        )
    
@student_router.put("/students/{stduent_id}")
def update_student(student_id : int, student: StudentCreate,db:Session = Depends(get_db)):
    try:
        service_logic = Servicelayer(db_session=db)           
        service_response = service_logic.update_student_details(student_id,student)
        return service_response
    except:
        raise HTTPException(
            detail = "could not found the student detail", status_code = 400
        )
    
@student_router.delete("/students/{student_id}")
def delete_student(student_id : int, db:Session = Depends(get_db)):
    
    service_logic = Servicelayer(db_session=db)
    service_response = service_logic.remove_a_student(student_id)
       
    if service_response is None:
        raise HTTPException (
            detail = "student details not found", status_code = 400
        )
    return {"message": f"student with id {student_id} deleted successfully"}

