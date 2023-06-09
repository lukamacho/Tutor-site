import shutil

import aiofiles as aiofiles
from fastapi import APIRouter, Depends, Query, UploadFile, File
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


class UploadProfilePictureRequest(BaseModel):
    file: UploadFile = File(...)


# @tutor_api.get("/tutor/{tutor_mail}")
# def get_tutor(tutor_mail: str, core: OlympianTutorService = Depends(get_core)):
#     tutor = core.get_tutor(tutor_mail)
#     core.change_tutor_first_name(tutor_mail, tutor.first_name)
#     core.change_tutor_last_name(tutor_mail, tutor.last_name)
#     core.change_tutor_biography(tutor_mail, tutor.biography)
#     pass

@tutor_api.post("/upload-profile-picture")
def upload_profile_picture(file: UploadFile = File(...)):
    file_path = "/path/to/destination/profile_picture.png"  # Specify the desired file path
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "Profile picture uploaded successfully!"}
@tutor_api.get("/tutor/{tutor_mail}")
async def get_tutor_profile(tutor_mail: str, core: OlympianTutorService = Depends(get_core)):
    # Fetch tutor profile logic here using the email parameter
    print(tutor_mail)

    tutor_profile = {
        "id": 1,
        "name": "John Doe",
        "email": tutor_mail,
        "bio": "I'm a tutor",
        "profilePicture": "/path/to/destination/profile_picture.png"
    }
    return core.tutor_interactor.get_tutor(tutor_mail)


@tutor_api.post("/tutor/change_bio")
def tutor_change_bio(change_bio: ChangeBioRequest, core: OlympianTutorService = Depends(get_core)):
    tutor_mail = change_bio.tutor_mail
    new_bio = change_bio.new_bio
    print(change_bio)
    tutor = core.tutor_interactor.get_tutor(tutor_mail)
    if tutor is None:
        return {"message":"No such tutor exists."}
    core.tutor_interactor.change_tutor_biography(tutor_mail,new_bio)
    return {"message": "Bio changed successfully!"}

@tutor_api.post("/withdrawal_request")
def tutor_change_bio(withdrawal_request: MoneyWithdrawalRequest, core: OlympianTutorService = Depends(get_core)):
    tutor_mail = withdrawal_request.tutor_mail
    amount = withdrawal_request.amount
    print(withdrawal_request)
    tutor = core.tutor_interactor.get_tutor(tutor_mail)
    if tutor is None:
        return {"message":"No such tutor exists."}
    tutor_balance = core.tutor_interactor.get_tutor_balance(tutor_mail)
    if amount > tutor_balance:
        return {"message": "Not enough money on your balance"}
    core.tutor_interactor.decrease_tutor_balance(tutor_mail,amount)
    return {"message": "Money withdrawal successfully!"}

@tutor_api.post("/tutor/upload_profile_picture/{tutor_mail}")
async def create_upload_file(
        tutor_mail: str,
        file: UploadFile = File(...),
        core: OlympianTutorService = Depends(get_core),
):
    dest_path = '../../frontend/src/Storage/' + tutor_mail
    async with aiofiles.open(dest_path, 'wb') as dest_file:
        content = await file.read()
        await dest_file.write(content)

    core.tutor_interactor.change_tutor_profile_address(tutor_mail, dest_path)