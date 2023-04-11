from fastapi import APIRouter

admin_api = APIRouter()


@admin_api.get("/admin")
def get_admin():
    pass
