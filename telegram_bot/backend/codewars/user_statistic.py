import requests

from codewars.models_user_statistic import (
    CodeWarsFullStatistic,
    CodeWarsMinStatistic,
)
from config import settings
from db.crud.users import (
    get_nickname,
    UserNotFoundException,
)


def get_user_statistic_by_nickname(
    nickname: str,
    full_statistic: bool,
) -> CodeWarsMinStatistic | CodeWarsFullStatistic | None:
    response = requests.get(settings.codewars_get_user_url + nickname)

    if response.status_code != 200:
        raise UserNotFoundException(nickname)

    response_json = response.json()

    if full_statistic:
        return CodeWarsFullStatistic(**response_json)

    return CodeWarsMinStatistic(
        honor=response_json.get("honor"),
        skills=response_json.get("skills"),
        ranks=response_json.get("ranks"),
        codeChallenges=response_json.get("codeChallenges"),
    )


def get_user_statistic_by_telegram_id(
    telegram_id: int,
    full_statistic: bool = False,
) -> CodeWarsMinStatistic | CodeWarsFullStatistic | None:
    return get_user_statistic_by_nickname(
        get_nickname(telegram_id),
        full_statistic,
    )
