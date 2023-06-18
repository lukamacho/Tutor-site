import aiofiles
from fastapi import APIRouter, Depends, File, UploadFile
from pydantic import BaseModel

from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core

tutor_api = APIRouter()


class ChangeBioRequest(BaseModel):
    tutor_mail: str
    new_bio: str


class MoneyWithdrawalRequest(BaseModel):
    tutor_mail: str
    amount: int


class CourseAdditionRequest(BaseModel):
    tutor_mail: str
    course_name: str
    course_price: int


class CourseDeletionRequest(BaseModel):
    tutor_mail: str
    course_name: str


@tutor_api.get("/tutor/{tutor_mail}")
async def get_tutor_profile(
    tutor_mail: str, core: OlympianTutorService = Depends(get_core)
):
    # Fetch tutor profile logic here using the email parameter
    print(tutor_mail)
    return core.tutor_interactor.get_tutor(tutor_mail)


@tutor_api.get("/tutor/courses/{tutor_mail}")
async def get_tutor_courses(
    tutor_mail: str, core: OlympianTutorService = Depends(get_core)
):
    # Fetch tutor profile logic here using the email parameter
    print(tutor_mail)
    tutor_courses = core.course_interactor.get_tutor_courses(tutor_mail)
    print(tutor_courses)
    return tutor_courses


@tutor_api.post("/tutor/change_bio")
def tutor_change_bio(
    change_bio: ChangeBioRequest, core: OlympianTutorService = Depends(get_core)
):
    tutor_mail = change_bio.tutor_mail
    new_bio = change_bio.new_bio
    print(change_bio)
    tutor = core.tutor_interactor.get_tutor(tutor_mail)
    if tutor is None:
        return {"message": "No such tutor exists."}
    core.tutor_interactor.change_tutor_biography(tutor_mail, new_bio)
    return {"message": "Bio changed successfully!"}


@tutor_api.post("/withdrawal_request")
def tutor_withdrawal_request(
    withdrawal_request: MoneyWithdrawalRequest,
    core: OlympianTutorService = Depends(get_core),
):
    tutor_mail = withdrawal_request.tutor_mail
    amount = withdrawal_request.amount
    print(withdrawal_request)
    tutor = core.tutor_interactor.get_tutor(tutor_mail)
    if tutor is None:
        return {"message": "No such tutor exists."}
    tutor_balance = core.tutor_interactor.get_tutor_balance(tutor_mail)
    if amount > tutor_balance:
        return {"message": "Not enough money on your balance"}
    core.tutor_interactor.decrease_tutor_balance(tutor_mail, amount)
    return {"message": "Money withdrawal successfully!"}


@tutor_api.post("/tutor/upload_profile_picture/{tutor_mail}")
async def create_upload_file(
    tutor_mail: str,
    file: UploadFile = File(...),
    core: OlympianTutorService = Depends(get_core),
):
    dest_path = "../../frontend/src/Storage/" + tutor_mail
    async with aiofiles.open(dest_path, "wb") as dest_file:
        content = await file.read()
        await dest_file.write(content)
    
    core.tutor_interactor.change_tutor_profile_address(tutor_mail, dest_path)


@tutor_api.post("/tutor/add_course")
async def add_course(
    course_addition: CourseAdditionRequest,
    core: OlympianTutorService = Depends(get_core),
):
    print(course_addition)
    tutor_mail = course_addition.tutor_mail
    course_name = course_addition.course_name
    course_price = course_addition.course_price
    if course_price <= 0:
        return {"message": "Course price can not be negative!"}
    tutor = core.tutor_interactor.get_tutor(tutor_mail)

    if tutor is None:
        return {"message": "No such tutor exists!"}

    core.course_interactor.create_course(course_name, tutor_mail, course_price)


@tutor_api.delete("/tutor/delete_course")
def delete_course(
    course_deletion: CourseDeletionRequest,
    core: OlympianTutorService = Depends(get_core),
):
    print(course_deletion)
    course_name = course_deletion.course_name
    tutor_mail = course_deletion.tutor_mail
    core.course_interactor.delete_course(tutor_mail, course_name)
