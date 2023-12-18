from pymongo import MongoClient

client = MongoClient("localhost",
                     27017)
db = client.users
collection = db.users


def create_user(nickname: str | None, telegram_id: int):
    if isinstance(nickname, str) == True or nickname == None \
            and isinstance(telegram_id, int) == True:
        create_user_model = {"_id": telegram_id,
                             "name": nickname}
        db.users.insertOne(create_user_model)
        return create_user_model
    else:
        return print("Введен не правильный тип данных")
