from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client.user
collection = db.users
test1_nickname = 'eytes'
test1_telegram_id = 12312
def create_user(nickname:str or None, telegram_id: int):
    if isinstance(nickname,str) == True and isinstance(nickname,None) == True and isinstance(telegram_id,int)
        create_user_model = {"_id": telegram_id,
                             "name": nickname}
        db.users.insertOne(create_user_model)
        return create_user_model
    else:
        return "Введен не правильный тип данных"
create_user(test1_nickname,test1_telegram_id)