from fastapi import APIRouter, Depends

from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core

student_api = APIRouter()


@student_api.get("/student/{student_mail}")
def get_student(
    student_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    student = core.get_student(student_mail)
    core.change_student_last_name(student_mail, student.last_name)
    core.change_student_first_name(student_mail, student.first_name)
    pass
