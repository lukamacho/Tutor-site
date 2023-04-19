from starlette.requests import Request

from app.core.facade import OlympianTutorService


def get_core(request: Request) -> OlympianTutorService:
    olympian_tutors: OlympianTutorService = request.app.state.core
    return olympian_tutors
