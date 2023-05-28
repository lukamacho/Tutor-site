from fastapi.applications import FastAPI

from app.infra.fastapi.admin_api import admin_api
from app.infra.fastapi.homepage_api import homepage_api
from app.infra.fastapi.student_api import student_api
from app.infra.fastapi.tutor_api import tutor_api
from app.core.facade import OlympianTutorService
from fastapi.middleware.cors import CORSMiddleware


def setup_fastapi(core: OlympianTutorService) -> FastAPI:
    app = FastAPI()

    origins = [
        "*"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(admin_api)
    app.include_router(homepage_api)
    app.include_router(student_api)
    app.include_router(tutor_api)

    app.state.core = core

    return app
