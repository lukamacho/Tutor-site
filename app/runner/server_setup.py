from typing import Protocol

from fastapi import FastAPI

from app.infra.fastapi.api_main import setup_fastapi


def setup() -> FastAPI:
    return setup_fastapi()

