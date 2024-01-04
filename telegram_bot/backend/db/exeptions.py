from fastapi import (
    HTTPException,
    status,
)

from config import settings


class NotFoundException(HTTPException):
    def __init__(self, identifier: int | str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=settings.detail_not_found(identifier),
        )


class UserNotFoundException(NotFoundException):
    pass


class NicknameNotFoundException(NotFoundException):
    pass


class UserExistException(HTTPException):
    def __init__(self, telegram_id: int):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=settings.detail_already_exists(telegram_id),
        )
