from fastapi import APIRouter

tutor_api = APIRouter()


@tutor_api.get("/tutor/{tutor_id}")
def get_tutor():
    pass
