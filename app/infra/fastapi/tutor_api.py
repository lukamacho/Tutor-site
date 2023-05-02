from fastapi import APIRouter, Depends

from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core

tutor_api = APIRouter()


@tutor_api.get("/tutor/{tutor_mail}")
def get_tutor(tutor_mail: str, core: OlympianTutorService = Depends(get_core)):
    tutor = core.get_tutor(tutor_mail)
    core.change_tutor_first_name(tutor_mail, tutor.first_name)
    core.change_tutor_last_name(tutor_mail, tutor.last_name)
    core.change_tutor_biography(tutor_mail, tutor.biography)
    pass
