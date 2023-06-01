import smtplib
import ssl
from random import choices
from string import ascii_letters, digits

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from pydantic import BaseModel
import requests

from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core
from app.infra.fastapi.homepage_api import hash_password

admin_api = APIRouter()

GOOGLE_CLIENT_ID = "your_client_id"
GOOGLE_CLIENT_SECRET = "your_client_secret"
GOOGLE_REDIRECT_URI = "your_redirect_uri"


class PasswordResetRequest(BaseModel):
    user_mail: str
    is_student: bool


class StudentDeleteRequest(BaseModel):
    student_mail: str


class TutorDeleteRequest(BaseModel):
    tutor_mail: str


class TutorCommissionRequest(BaseModel):
    tutor_mail: str


class SingInRequest(BaseModel):
    user_mail: str
    password: str
    is_student: bool


class BalanceAdditionRequest(BaseModel):
    student_mail: str
    amount: int


class DecreaseBalanceRequest(BaseModel):
    tutor_mail: str
    amount: int


def generate_new_password() -> str:
    # Generate a random password
    password_length = 8
    characters = ascii_letters + digits
    new_password = "".join(choices(characters, k=password_length))
    return new_password


def send_new_password(receiver_mail: str) -> str:
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "tutorsite727@gmail.com"
    password = "fvqxtupjruxqcooo"

    context = ssl.create_default_context()
    new_password = generate_new_password()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_mail, new_password)
    return new_password


@admin_api.get("/admin/hello")
def get_admin(core: OlympianTutorService = Depends(get_core)):
    print("hello sender")
    core.admin_interactor.send_verification()


@admin_api.delete("/admin/delete_student")
def delete_student(
    student_mail: StudentDeleteRequest, core: OlympianTutorService = Depends(get_core)
):
    print(student_mail)
    student = core.tutor_interactor.get_tutor(student_mail)
    if student is None:
        return {"message": "Student with this mail doesn't exist!"}
    core.student_interactor.delete_student(student_mail.student_mail)
    return {"message": "Student deleted successfully"}


@admin_api.delete("/admin/delete_tutor")
def delete_tutor(
    tutor_mail: TutorDeleteRequest, core: OlympianTutorService = Depends(get_core)
):
    print(tutor_mail)
    tutor = core.tutor_interactor.get_tutor(tutor_mail.tutor_mail)
    if tutor is None:
        return {"message": "Tutor with this mail doesn't exist!"}
    core.tutor_interactor.delete_tutor(tutor_mail.tutor_mail)
    return {"message": "Tutor deleted successfully"}


@admin_api.delete("/admin/commission_pct")
def commission_tutor(
    tutor_mail: TutorCommissionRequest, core: OlympianTutorService = Depends(get_core)
):
    print(tutor_mail)
    tutor = core.tutor_interactor.get_tutor(tutor_mail.tutor_mail)
    if tutor is None:
        return {"message": "Tutor with this mail doesn't exist!"}
    core.tutor_interactor.decrease_commission_pct(tutor_mail.tutor_mail)

    return {"message": "Commission_pct decreased successfully"}


@admin_api.post("/admin/reset_password")
def reset_password(
    password_reset: PasswordResetRequest, core: OlympianTutorService = Depends(get_core)
):
    user_mail = password_reset.user_mail
    is_student = password_reset.is_student
    print(password_reset)
    if is_student:
        student = core.get_student(user_mail)
        if student is None:
            raise HTTPException(status_code=404, detail="Email not found")
        new_password = send_new_password(user_mail)
        new_password = hash_password(new_password)
        core.student_interactor.change_student_password(user_mail, new_password)
    else:
        tutor = core.get_tutor(user_mail)
        if tutor is None:
            raise HTTPException(status_code=404, detail="Email not found")
        new_password = send_new_password(user_mail)
        new_password = hash_password(new_password)
        core.tutor_interactor.change_tutor_password(user_mail, new_password)

    return {"message": "Password resat successfully."}


@admin_api.post("/sign_in")
def sign_in(
    sign_in_request: SingInRequest, core: OlympianTutorService = Depends(get_core)
):
    print(sign_in_request)
    is_student = sign_in_request.is_student
    user_mail = sign_in_request.user_mail
    user_password = hash_password(sign_in_request.password)
    if is_student:
        student = core.student_interactor.get_student(user_mail)
        if student is None:
            raise HTTPException(502, "No such student exists.")
        if student.password != user_password:
            raise HTTPException(501, "Password is incorrect.")
        print(user_password)
    else:
        tutor = core.tutor_interactor.get_tutor(user_mail)
        if tutor is None:
            raise HTTPException(502, "No such tutor exists.")
        if tutor.password != user_password:
            raise HTTPException(501, "Password is incorrect")

        print(user_password)
    return {"message": "User sign in successfully."}


@admin_api.get("/google_sign_in")
def google_sign_in():
    # Generate and return the Google OAuth2 authorization URL
    authorization_url = generate_google_auth_url()
    return {"authorization_url": authorization_url}


@admin_api.get("/google_sign_in_callback")
def google_sign_in_callback(code: str):
    # Handle the Google sign-in callback here
    try:
        token_response = exchange_code_for_token(code)
        user_info = get_user_info(token_response["access_token"])
        # Process user_info as needed
        # ...
        # Redirect the user to the desired page after successful authentication
        redirect_url = "http://localhost:3000/"  # Change this to the desired URL
        return RedirectResponse(redirect_url)
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": "Google sign-in failed."}
        )


def generate_google_auth_url():
    # Construct the Google OAuth2 authorization URL
    auth_endpoint = "https://accounts.google.com/o/oauth2/auth"
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
    }
    auth_url = f"{auth_endpoint}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
    return auth_url


def exchange_code_for_token(code: str):
    token_endpoint = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_endpoint, data=data)
    response.raise_for_status()
    return response.json()


def get_user_info(access_token: str):
    user_info_endpoint = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(user_info_endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


@admin_api.post("/admin/increase_student_balance")
def add_balance(
    add_balance: BalanceAdditionRequest, core: OlympianTutorService = Depends(get_core)
):
    student_mail = add_balance.student_mail
    amount = add_balance.amount
    student = core.student_interactor.get_student(student_mail)
    if student is None:
        return {"Message": "No such student exists."}
    core.student_interactor.increase_student_balance(student_mail, amount)

    return {"message": "Balance added successfully."}


@admin_api.post("/admin/decrease_tutor_balance")
def decrease_balance(
    decrease_balance: DecreaseBalanceRequest,
    core: OlympianTutorService = Depends(get_core),
):
    tutor_mail = decrease_balance.tutor_mail
    amount = decrease_balance.amount
    tutor = core.tutor_interactor.get_tutor(tutor_mail)
    if tutor is None:
        return {"Message": "No such tutor exists."}
    core.tutor_interactor.decrease_tutor_balance(tutor_mail, amount)
    return {"message": "Balance decreased successfully."}
