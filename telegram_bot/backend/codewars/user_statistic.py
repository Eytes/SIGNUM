import requests

from db.crud.users import (
    get_nickname,
    UserNotFoundError,
)
from db.exeptions import UserWithoutNicknameError
from codewars.models_user_statistic import (
    CodeWarsFullUserStatistic,
    CodeWarsMinUserStatistic,
)

CODEWARS_GET_USER_URL = 'https://www.codewars.com/api/v1/users/{nickname}'


def get_user_statistic_by_nickname(
        nickname: str,
        full_statistic: bool
) -> CodeWarsMinUserStatistic | CodeWarsFullUserStatistic | None:
    try:
        response = requests.get(CODEWARS_GET_USER_URL.format(nickname=nickname))

        if response.status_code == 404:
            raise UserNotFoundError(nickname=nickname)

        response_json = response.json()

        if full_statistic:
            return CodeWarsFullUserStatistic(**response_json)
        return CodeWarsMinUserStatistic(
            honor=response_json.get('honor'),
            skills=response_json.get('skills'),
            ranks=response_json.get('ranks'),
            codeChallenges=response_json.get('codeChallenges'),
        )

    except (UserWithoutNicknameError, UserNotFoundError):
        return None


def get_user_statistic_by_telegram_id(
        telegram_id: int,
        full_statistic: bool = False
) -> CodeWarsMinUserStatistic | CodeWarsFullUserStatistic | None:
    try:
        nickname = get_nickname(telegram_id)
        return get_user_statistic_by_nickname(nickname, full_statistic)

    except (UserWithoutNicknameError, UserNotFoundError):
        return None
