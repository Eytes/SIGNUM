class UserWithoutNickname(Exception):
    def __init__(self):
        super().__init__('У пользователя нет зарегистрированного nickname codewars')
