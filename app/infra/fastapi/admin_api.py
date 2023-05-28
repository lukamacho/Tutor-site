from fastapi import APIRouter, Depends

from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core
from pydantic import BaseModel
admin_api = APIRouter()

class StudentDeleteRequest(BaseModel):
    student_mail: str

class TutorDeleteRequest(BaseModel):
    tutor_mail: str

class TutorCommissionRequest(BaseModel):
    tutor_mail: str

@admin_api.get("/admin/hello")
def get_admin(core: OlympianTutorService = Depends(get_core)):
    print("hello sender")
    core.admin_interactor.send_verification()

@admin_api.delete("/admin/delete_student")
def delete_student(student_mail: StudentDeleteRequest,core: OlympianTutorService = Depends(get_core)):
    print(student_mail)

    return {"message": "Student deleted successfully"}


@admin_api.delete("/admin/delete_tutor")
def delete_tutor(tutor_mail: TutorDeleteRequest,core: OlympianTutorService = Depends(get_core)):
    print(tutor_mail)
    core.tutor_interactor.delete_tutor(tutor_mail.tutor_mail)
    return {"message": "Tutor deleted successfully"}


@admin_api.delete("/admin/commission_pct")
def commision_tutor(tutor_mail: TutorCommissionRequest,core: OlympianTutorService = Depends(get_core)):
    print(tutor_mail)
    core.tutor_interactor.decrease_commission_pct(tutor_mail.tutor_mail)

    return {"message": "Commission_pct decreased successfully"}



