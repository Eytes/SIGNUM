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
    response_json = requests.get(CODEWARS_GET_USER.format(nickname=nickname)).json()
    if full_statistic:
        return CodeWarsFullUserStatistic(**response_json)
    return CodeWarsMinUserStatistic(
        honor=response_json.get('honor'),
        skills=response_json.get('skills'),
        ranks=response_json.get('ranks'),
        code_challenges=response_json.get('code_challenges'),
    )


def get_user_statistic_by_telegram_id(
        telegram_id: int,
        full_statistic: bool = False
) -> CodeWarsMinUserStatistic | CodeWarsFullUserStatistic:
    nickname = get_nickname(telegram_id)
    if not nickname:
        raise UserWithoutNickname
    return get_user_statistic_by_nickname(nickname, full_statistic)
