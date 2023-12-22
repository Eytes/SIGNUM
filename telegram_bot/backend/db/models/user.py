from pydantic import (
    BaseModel,
    Field,
)


class User(BaseModel):
    telegram_id: int = Field(alias='_id')  # такой alias для mongodb
    username: str
