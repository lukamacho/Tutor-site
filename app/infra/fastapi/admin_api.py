from fastapi import APIRouter,Depends

from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core

admin_api = APIRouter()


@admin_api.get("/admin/hello")
def get_admin(core: OlympianTutorService = Depends(get_core)):
    core.send_hello()
    pass
