from fastapi import APIRouter
import requests

CODEWARS_GET_USER = 'https://www.codewars.com/api/v1/users/{user}'

router = APIRouter(
    prefix='/user'
)


@router.get('/full_statistic/{telegram_id}')
def get_full_statistic(telegram_id: int) -> dict:
    # TODO: запрос в бд для получения имени пользователя
    # TODO: полученное имя используем для отправки запроса на codewars
    # TODO: из ответа от сервера codewars выбираем только нужную информацию и отдаем ее на frontend
    return {"msg": "Hello World"}


@router.get('/min_statistic/{telegram_id}')
def get_min_statistic(telegram_id: int) -> dict:
    # TODO: запрос в бд для получения имени пользователя
    # TODO: полученное имя используем для отправки запроса на codewars
    # TODO: из ответа от сервера codewars выбираем только нужную информацию и отдаем ее на frontend
    return {"msg": "Hello World"}
