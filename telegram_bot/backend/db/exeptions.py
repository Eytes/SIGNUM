class UserWithoutNicknameError(Exception):
    def __init__(self, telegram_id: int):
        super().__init__(f'У пользователя {telegram_id=} нет зарегистрированного nickname codewars')


class UserNotFoundError(Exception):
    def __init__(self, *, telegram_id: int | None = None, nickname: str | None = None):
        match telegram_id, nickname:
            case (_, _) | (_, None):
                super().__init__(f'Пользователь с {telegram_id=} не найден')
            case (None, _):
                super().__init__(f'Пользователь с {nickname=} не найден')


class UserExistError(Exception):
    def __init__(self, telegram_id: int):
        super().__init__(f'Пользователь с {telegram_id=} уже существует')
