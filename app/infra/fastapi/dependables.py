from starlette.requests import Request

from app.core.facade import OlympianTutorService


def get_core(request: Request) -> OlympianTutorService:
    btc_wallet_service:OlympianTutorService = request.app.state.core
    return btc_wallet_service
