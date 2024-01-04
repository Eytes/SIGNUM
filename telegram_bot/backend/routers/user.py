from fastapi import (
    APIRouter,
    status,
)
from fastapi.responses import JSONResponse

from codewars.user_statistic import (
    get_user_statistic_by_telegram_id,
    get_user_statistic_by_nickname,
)

router = APIRouter(
    prefix='/user'
)


@router.get('/statistic_by_telegram_id/{show_full_statistic}/{telegram_id}')
def get_statistic_by_telegram_id(show_full_statistic: bool, telegram_id: int) -> JSONResponse:
    statistic = get_user_statistic_by_telegram_id(telegram_id, show_full_statistic)
    if not statistic:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": 'not found'})
    return JSONResponse(status_code=status.HTTP_200_OK, content=statistic.model_dump(by_alias=True))


@router.get('/statistic_by_codewars_nickname/{show_full_statistic}/{nickname}')
def get_statistic_by_codewars_nickname(show_full_statistic: bool, nickname: str):
    statistic = get_user_statistic_by_nickname(nickname, show_full_statistic)
    if not statistic:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": 'not found'})
    return JSONResponse(status_code=status.HTTP_200_OK, content=statistic.model_dump(by_alias=True))
