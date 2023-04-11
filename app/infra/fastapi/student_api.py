from fastapi import APIRouter

student_api = APIRouter()


@student_api.get("/student/{student_id}")
def get_student(student_id: int):
    pass

