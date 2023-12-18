from db.models.user import User
from db.crud.common import *
from db.collections import users


def get_by_telegram_id(telegram_id: int) -> dict:
    """
    Хендлер для получения пользователя по его telegram id
    """
    return get_document(
        users,
        {"telegram_id": telegram_id},
    )


def get_by_nickname(nickname: str) -> dict:
    """
    Хендлер для получения пользователя по его nickname на codewars
    """
    return get_document(
        users,
        {"nickname": nickname},
    )


def create(user_data: User) -> str:
    """
    Хендлер создания пользователя
    """
    return create_document(
        users,
        user_data.model_dump(by_alias=True),
    )


def update(telegram_id: int, new_value: dict) -> None:
    """
    Хендлер обновление данных о пользователе
    """
    update_document(
        users,
        {"telegram_id": telegram_id},
        new_value,
    )


def delete_by_telegram_id(telegram_id: int) -> None:
    """
    Хендлер для удаления пользователя
    """
    delete_document(
        users,
        {"telegram_id": telegram_id},
    )


def get_nickname(telegram_id: int) -> str | None:
    """
    Хендлер для получения имени пользователя на codewars
    """
    return get_by_telegram_id(telegram_id).get('nickname', None)
