from pymongo import MongoClient
from pymongo.collection import Collection

_client = MongoClient(
    'mongodb://mongodb:27017/',
    UuidRepresentation='standard',  # чтобы uuid генерировалось синхронизировано с python
)  # cluster
_db = _client['ProstoYoga']  # create database

# create collections
teams: Collection = _db['teams']
users: Collection = _db['users']
students: Collection = users['students']  # подколлекция users
teachers: Collection = users['teachers']  # подколлекция users
