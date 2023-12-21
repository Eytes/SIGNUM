from enum import Enum

from fastapi import (
    APIRouter,
    status,
)
from fastapi.responses import JSONResponse

from codewars.user_statistic import get_user_statistic_by_telegram_id

router = APIRouter(
    prefix='/user'
)


class UserStatisticFormat(str, Enum):
    full = True
    min = False


@router.get('/statistic/{show_full_statistic}/{telegram_id}')
def get_statistic(show_full_statistic: UserStatisticFormat, telegram_id: int) -> JSONResponse:
    statistic = get_user_statistic_by_telegram_id(telegram_id, show_full_statistic.value)
    if not statistic:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'detail': 'User not found'})
    return JSONResponse(status_code=status.HTTP_200_OK, content=statistic.model_dump(by_alias=True))
