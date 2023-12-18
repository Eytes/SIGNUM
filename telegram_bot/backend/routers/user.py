from fastapi import APIRouter

from codewars.user_statistic import get_user_statistic_by_telegram_id


router = APIRouter(
    prefix='/user'
)


@router.get('/full_statistic/{telegram_id}')
def get_full_statistic(telegram_id: int) -> dict:
    statistic = get_user_statistic_by_telegram_id(telegram_id, True)
    return statistic.model_dump(by_alias=True)


@router.get('/min_statistic/{telegram_id}')
def get_min_statistic(telegram_id: int) -> dict:
    statistic = get_user_statistic_by_telegram_id(telegram_id)
    return statistic.model_dump(by_alias=True)
