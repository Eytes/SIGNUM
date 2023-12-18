import requests

from db.crud.users import *
from db.exeptions import UserWithoutNickname
from codewars.models_user_statistic import (
    CodeWarsFullUserStatistic,
    CodeWarsMinUserStatistic,
)

CODEWARS_GET_USER = 'https://www.codewars.com/api/v1/users/{nickname}'


def get_user_statistic_by_nickname(
        nickname: str,
        full_statistic: bool = False
) -> CodeWarsMinUserStatistic | CodeWarsFullUserStatistic:
    response = requests.get(CODEWARS_GET_USER.format(nickname=nickname))
    if full_statistic:
        return CodeWarsFullUserStatistic(**response.json())
    return CodeWarsMinUserStatistic(**response.json())


def get_user_statistic_by_telegram_id(
        telegram_id: int,
        full_statistic: bool = False
) -> CodeWarsMinUserStatistic | CodeWarsFullUserStatistic:
    nickname = get_nickname(telegram_id)
    if not nickname:
        raise UserWithoutNickname
    return get_user_statistic_by_nickname(nickname, full_statistic)
