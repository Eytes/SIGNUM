from db.models.user import CreateUser
from db.collections import users
from db.crud.common import (
    create_document,
    get_document,
    update_document,
    delete_document,
)
from db.exeptions import (
    UserNotFoundException,
    UserExistException,
    NicknameNotFoundException,
)
from db.models.user import User


def _user_exists(telegram_id: int) -> bool:
    user = get_document(
        users,
        {"telegram_id": telegram_id},
    )
    return True if user else False


def get_by_telegram_id(telegram_id: int) -> User:
    """Хендлер для получения пользователя по его telegram id"""
    user = get_document(
        users,
        {"telegram_id": telegram_id},
    )
    if not user:
        raise UserNotFoundException(telegram_id)
    return User(**user)


def get_by_nickname(nickname: str) -> User:
    """Хендлер для получения пользователя по его nickname на codewars"""
    user = get_document(
        users,
        {"nickname": nickname},
    )
    if not user:
        raise NicknameNotFoundException(nickname)
    return User(**user)



def create(user_data: User) -> str:
    """Хендлер создания пользователя"""
    if _user_exists(user_data.telegram_id):
        raise UserExistException(user_data.telegram_id)
    return create_document(
        users,
        user_data.model_dump(by_alias=True),
    )


def update(telegram_id: int, new_value: dict) -> None:
    """Хендлер обновление данных о пользователе"""
    if not _user_exists(telegram_id):
        raise UserNotFoundException(telegram_id)
    update_document(
        users,
        {"telegram_id": telegram_id},
        new_value,
    )


def delete(telegram_id: int) -> None:
    """Хендлер для удаления пользователя"""
    if not _user_exists(telegram_id):
        raise UserNotFoundException(telegram_id)
    delete_document(
        users,
        {"telegram_id": telegram_id},
    )


def get_nickname(telegram_id: int) -> str | None:
    """Хендлер для получения имени пользователя на codewars"""
    return get_by_telegram_id(telegram_id).get("nickname")


def update_nickname(telegram_id: int, new_nickname: str):
    """Обновление nickname пользователя"""
    update(telegram_id, {"nickname": new_nickname})
