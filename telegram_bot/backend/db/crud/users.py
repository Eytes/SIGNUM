from db.models.user import CreateUser
from db.crud.common import (
    create_document,
    get_document,
    update_document,
    delete_document,
)
from db.collections import users
from db.exeptions import (
    UserNotFoundError,
    UserExistError,
    UserWithoutNicknameError,
)


def user_exists(telegram_id: int) -> bool:
    user = get_document(
        users,
        {"telegram_id": telegram_id},
    )
    return True if user else False


def get_by_telegram_id(telegram_id: int) -> dict:
    """
    Хендлер для получения пользователя по его telegram id
    """
    user = get_document(
        users,
        {"telegram_id": telegram_id},
    )
    if not user:
        raise UserNotFoundError(telegram_id=telegram_id)
    return user


def get_by_nickname(nickname: str) -> dict:
    """
    Хендлер для получения пользователя по его nickname на codewars
    """
    user = get_document(
        users,
        {"nickname": nickname},
    )
    if not user:
        raise UserNotFoundError(nickname=nickname)
    return user


def create(user_data: CreateUser) -> str:
    """
    Хендлер создания пользователя
    """
    if user_exists(user_data.telegram_id):
        raise UserExistError(user_data.telegram_id)
    return create_document(
        users,
        user_data.model_dump(by_alias=True),
    )


def update(telegram_id: int, new_value: dict) -> None:
    """
    Хендлер обновление данных о пользователе
    """
    if not user_exists(telegram_id):
        raise UserNotFoundError(telegram_id=telegram_id)
    update_document(
        users,
        {"telegram_id": telegram_id},
        new_value,
    )


def delete(telegram_id: int) -> None:
    """
    Хендлер для удаления пользователя
    """
    if not user_exists(telegram_id):
        raise UserNotFoundError(telegram_id=telegram_id)
    delete_document(
        users,
        {"telegram_id": telegram_id},
    )


def get_nickname(telegram_id: int) -> str:
    """
    Хендлер для получения имени пользователя на codewars
    """
    nickname = get_by_telegram_id(telegram_id).get('nickname')
    if not nickname:
        raise UserWithoutNicknameError(telegram_id)
    return nickname


def update_nickname(telegram_id: int, new_nickname: str):
    """
    Обновление nickname пользователя
    """
    update(telegram_id, {'nickname': new_nickname})
