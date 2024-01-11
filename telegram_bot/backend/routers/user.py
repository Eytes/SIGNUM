from fastapi import (
    APIRouter,
    status,
)
from fastapi.responses import JSONResponse

from codewars.user_statistic import (
    get_user_statistic_by_telegram_id,
    get_user_statistic_by_nickname,
)
from db.exeptions import UserExistError
from db.models.user import CreateUser
from db.crud import users as users_crud


router = APIRouter(tags=["Users"])


@router.get(
    "/statistic_by_telegram_id/{show_full_statistic}/{telegram_id}",
    status_code=status.HTTP_200_OK,
)
def get_statistic_by_telegram_id(
    show_full_statistic: bool,
    telegram_id: int,
) -> JSONResponse:
    statistic = get_user_statistic_by_telegram_id(telegram_id, show_full_statistic)
    if not statistic:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": "not found"},
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=statistic.model_dump(by_alias=True),
    )


@router.get(
    "/statistic_by_codewars_nickname/{show_full_statistic}/{nickname}",
    status_code=status.HTTP_200_OK,
)
def get_statistic_by_codewars_nickname(show_full_statistic: bool, nickname: str):
    statistic = get_user_statistic_by_nickname(nickname, show_full_statistic)
    if not statistic:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": 'not found'})
    return JSONResponse(status_code=status.HTTP_200_OK, content=statistic.model_dump(by_alias=True))


@router.post('/')
def create_user(new_user: CreateUser):
    try:
        return users_crud.create(new_user)
    except UserExistError:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": "not found"},
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=statistic.model_dump(by_alias=True),
    )


@router.get(
    "/users/telegram_id/{telegram_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
def get_user_by_telegram_id(telegram_id: int):
    return users_crud.get_by_telegram_id(telegram_id)


@router.get(
    "/users/nickname/{nickname}",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
def get_user_by_nickname(nickname: str):
    return users_crud.get_by_nickname(nickname)

