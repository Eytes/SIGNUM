from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    prefix_api_v1 = "/api/v1"
    codewars_get_user_url = "https://www.codewars.com/api/v1/users/"

    @staticmethod
    def detail_not_found(identifier: int | str):
        return f"User with {identifier=} not found!"

    @staticmethod
    def detail_already_exists(identifier: int | str):
        return f"User with {identifier=} already exists!"


settings = Settings()
