import smtplib
import ssl
from datetime import datetime
from random import choices
from string import ascii_letters, digits
from typing import Any, Dict

from app.infra.fastapi.token_authentication import generate_token, token_verification

import requests
from fastapi import APIRouter, Depends, HTTPException

from pydantic import BaseModel

from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core
from app.infra.fastapi.homepage_api import hash_password

admin_api = APIRouter()

GOOGLE_CLIENT_ID = "your_client_id"
GOOGLE_CLIENT_SECRET = "your_client_secret"
GOOGLE_REDIRECT_URI = "your_redirect_uri"


class PasswordResetRequest(BaseModel):
    email: str


class StudentDeleteRequest(BaseModel):
    student_mail: str


class TutorDeleteRequest(BaseModel):
    tutor_mail: str


class TutorCommissionRequest(BaseModel):
    tutor_mail: str


class ReportToAdminRequest(BaseModel):
    report: str


class SingInRequest(BaseModel):
    email: str
    password: str


class BalanceAdditionRequest(BaseModel):
    student_mail: str
    amount: int


class DecreaseBalanceRequest(BaseModel):
    tutor_mail: str
    amount: int


class VerifyTokenRequest(BaseModel):
    token: str
    email: str


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


@admin_api.post("/admin/report_to_admin/{user_mail}")
async def report_to_admin(
    user_mail: str,
    data: ReportToAdminRequest,
) -> Dict[str, str]:
    print("/student/report_to_admin/" + user_mail)
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "tutorsite727@gmail.com"
    password = "fvqxtupjruxqcooo"
    message = user_mail + " [report] " + data.report

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(user_mail, sender_email, message)

    return {"message": "Sent a report to admin."}


@admin_api.delete("/admin/delete_student")
def delete_student(
    student_mail: StudentDeleteRequest, core: OlympianTutorService = Depends(get_core)
) -> Dict[str, str]:
    print(student_mail)
    student = core.student_interactor.get_student(student_mail.student_mail)
    if student.email == "":
        return {"message": "Student delete failed."}

    core.student_interactor.delete_student(student_mail.student_mail)
    return {"message": "Student deleted successfully"}


@admin_api.delete("/admin/delete_tutor")
def delete_tutor(
    tutor_mail: TutorDeleteRequest, core: OlympianTutorService = Depends(get_core)
) -> Dict[str, str]:
    print(tutor_mail)
    tutor = core.tutor_interactor.get_tutor(tutor_mail.tutor_mail)
    if tutor.email == "":
        return {"message": "Tutor with this mail doesn't exist!"}
    core.tutor_interactor.delete_tutor(tutor_mail.tutor_mail)
    return {"message": "Tutor deleted successfully"}


@admin_api.delete("/admin/commission_pct")
def commission_tutor(
    tutor_mail: TutorCommissionRequest, core: OlympianTutorService = Depends(get_core)
) -> Dict[str, str]:
    print(tutor_mail)
    tutor = core.tutor_interactor.get_tutor(tutor_mail.tutor_mail)
    if tutor.email == "":
        return {"message": "Tutor with this mail doesn't exist!"}
    core.tutor_interactor.decrease_commission_pct(tutor_mail.tutor_mail)

    return {"message": "Commission_pct decreased successfully"}


@admin_api.post("/admin/reset_password")
def reset_password(
    password_reset: PasswordResetRequest, core: OlympianTutorService = Depends(get_core)
) -> Dict[str, str]:
    user_mail = password_reset.email
    print(password_reset)
    student = core.get_student(user_mail)
    tutor = core.get_tutor(user_mail)
    if student.email == "" and tutor.email == "":
        raise HTTPException(status_code=505, detail="Email not found")
    if student.email != "":
        new_password = send_new_password(user_mail)
        new_password = hash_password(new_password)
        core.student_interactor.change_student_password(user_mail, new_password)
        return {"message": "Student password reset successfully."}
    if tutor.email != "":
        new_password = send_new_password(user_mail)
        new_password = hash_password(new_password)
        core.tutor_interactor.change_tutor_password(user_mail, new_password)
        return {"message": "Tutor password reset successfully."}

    return {"message": "Password reset successfully."}


@admin_api.post("/sign_in")
def sign_in(
    sign_in_request: SingInRequest, core: OlympianTutorService = Depends(get_core)
) -> Dict[str, object]:
    print(sign_in_request)

    email = sign_in_request.email
    password = hash_password(sign_in_request.password)

    tutor = core.tutor_interactor.get_tutor(email)
    student = core.student_interactor.get_student(email)

    token = generate_token(email)

    errorMessage = {
        "error": True,
        "token": "",
    }

    if tutor.email == "" and student.email == "":
        print("tutor is None and student is None")
        return errorMessage

    if tutor.email != "":
        if password != tutor.password:
            print("tutor is not None; password != tutor.password")
            return errorMessage
        else:
            print("tutor is not None; password == tutor.password")
            return {
                "error": False,
                "token": token,
                "is_student": False,
            }
    else:
        if password != student.password:
            print("student is not None; password != student.password")
            return errorMessage
        else:
            print("student is not None; password == student.password")
            return {
                "error": False,
                "token": token,
                "is_student": True,
            }


@admin_api.get("/google_sign_in")
def google_sign_in() -> Dict[str, str]:
    # Generate and return the Google OAuth2 authorization URL
    authorization_url = generate_google_auth_url()
    return {"authorization_url": authorization_url}


# @admin_api.get("/google_sign_in_callback")
# def google_sign_in_callback(code: str):
# Handle the Google sign-in callback here
#   try:
# token_response = exchange_code_for_token(code)
# user_info = get_user_info(token_response["access_token"])
# Process user_info as needed
# ...
# Redirect the user to the desired page after successful authentication
#      redirect_url = "http://localhost:3000/"  # Change this to the desired URL
#     return RedirectResponse(redirect_url)
# except Exception:
#    return JSONResponse(
#       status_code=400, content={"message": "Google sign-in failed."}
#   )


def generate_google_auth_url() -> str:
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


def exchange_code_for_token(code: str) -> Any:
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


def get_user_info(access_token: str) -> Any:
    user_info_endpoint = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(user_info_endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


@admin_api.post("/admin/increase_student_balance")
def add_balance(
    add_balance: BalanceAdditionRequest, core: OlympianTutorService = Depends(get_core)
) -> Dict[str, str]:
    student_mail = add_balance.student_mail
    amount = add_balance.amount
    student = core.student_interactor.get_student(student_mail)
    if student.email == "":
        return {"message": "No such student exists."}
    core.student_interactor.increase_student_balance(student_mail, amount)

    return {"message": "Balance added successfully."}


@admin_api.post("/admin/decrease_tutor_balance")
def decrease_balance(
    decrease_balance: DecreaseBalanceRequest,
    core: OlympianTutorService = Depends(get_core),
) -> Dict[str, str]:
    tutor_mail = decrease_balance.tutor_mail
    amount = decrease_balance.amount
    tutor = core.tutor_interactor.get_tutor(tutor_mail)
    if tutor.email == "":
        return {"Message": "No such tutor exists."}
    core.tutor_interactor.decrease_tutor_balance(tutor_mail, amount)
    return {"message": "Balance decreased successfully."}


@admin_api.post("/verify_token")
def verify_token(
    verify_token_request: VerifyTokenRequest,
) -> Dict[str, bool]:
    verifyToken = verify_token_request.token
    verifyMail = verify_token_request.email

    if verifyToken == "" or verifyMail == "":
        return {"verified": False}

    print(verifyToken)
    print(verifyMail)

    verification = token_verification(verifyToken)
    if verification == verifyMail:
        print("verified")
        return {"verified": True}
    else:
        print("not verified")
        return {"verified": False}


class MeetingLinkRequest(BaseModel):
    tutor_mail: str
    student_mail: str
    date_and_time: str


@admin_api.post("/generate_meeting_link")
async def generate_meeting_link(data: MeetingLinkRequest) -> Dict[str, str]:
    tutor_mail = data.tutor_mail
    student_mail = data.student_mail
    user_mails = [tutor_mail, student_mail]
    date_time = data.date_and_time
    print(date_time)
    # Split the date and time components
    date_parts = date_time.split("T")
    if len(date_parts) != 2:
        return {"error": "Invalid date and time format"}

    date = date_parts[0]
    time = date_parts[1]
    print("amas")
    # Split the time into hours and minutes
    print(time)
    time = date_parts[1].split(".")[0]
    time_parts = time.split(":")
    if len(time_parts) != 3:
        return {"error": "Invalid time format"}

    hour = int(time_parts[0])
    minute = int(time_parts[1])
    print(hour)
    print(minute)
    # Construct the start and end time objects
    start_time = datetime.strptime(date, "%Y-%m-%d").replace(hour=hour, minute=minute)
    # This must be but problems of mypy
    # end_time = start_time + timedelta(hours=1)  # Assuming a meeting duration of 1 hour
    end_time = start_time
    # Construct the event payload
    event = {
        "summary": "Meeting",
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "Your_Time_Zone",
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "Your_Time_Zone",
        },
        "attendees": [{"email": email} for email in user_mails],
        "conferenceData": {"createRequest": {"requestId": "random_id"}},
    }

    # Make a POST request to the Google Calendar API to create the event
    response = requests.post(
        "https://www.googleapis.com/calendar/v3/calendars/primary/events",
        headers={"Authorization": "Bearer YOUR_ACCESS_TOKEN"},
        json=event,
    )

    print(response.status_code)
    print(response.content)

    if response.status_code == 200:
        # Extract the meeting link from the API response
        meeting_link = response.json()["conferenceData"]["entryPoints"][0]["uri"]
        return {"meeting_link": meeting_link}
    else:
        return {"message": "Failed to create the meeting."}


class ScoreTutorRequest(BaseModel):
    tutor_mail: str
    score: int


@admin_api.post("/admin/score_tutor")
async def score_tutor(
    data: ScoreTutorRequest, core: OlympianTutorService = Depends(get_core)
) -> Dict[str, str]:
    tutor_mail = data.tutor_mail
    score = data.score
    tutor = core.tutor_interactor.get_tutor(tutor_mail)
    if tutor.email == "":
        return {"message": "Tutor with this mail doesn't exist"}
    core.tutor_ranking_interactor.set_admin_score(tutor_mail, score)

    return {"message": "Tutor evaluated successfully."}
