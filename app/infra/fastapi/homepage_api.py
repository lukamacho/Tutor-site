from fastapi import APIRouter

homepage_api = APIRouter()


@homepage_api.post("/")
def create_user():
    pass
