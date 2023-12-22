from typing import Any

from pydantic import (
    BaseModel,
    Field,
)


class CodeWarsFullUserStatistic(BaseModel):
    """
    Полная статистика пользователя
    """
    id: str
    username: str
    name: str | None
    honor: int
    clan: str | None
    leaderboard_position: int = Field(alias='leaderboardPosition')
    skills: list[str] | None
    ranks: dict[str, dict[str, Any]]
    code_challenges: dict[str, int] = Field(alias='codeChallenges')


class CodeWarsMinUserStatistic(BaseModel):
    """
    Минимально необходимая статистика пользователя
    """
    honor: int
    skills: list[str] | None
    ranks: dict[str, dict[str, Any]]
    code_challenges: dict[str, int] = Field(alias='codeChallenges')
