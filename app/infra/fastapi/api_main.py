from fastapi.applications import FastAPI

from app.infra.fastapi.admin_api import admin_api
from app.infra.fastapi.tutor_api import tutor_api
from app.infra.fastapi.homepage_api import homepage_api
from app.infra.fastapi.student_api import student_api

def setup_fastapi() -> FastAPI:
    app = FastAPI()

    app.include_router(admin_api)
    app.include_router(homepage_api)
    app.include_router(student_api)
    app.include_router(tutor_api)

    return app
