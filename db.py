import os
from pymongo import MongoClient


client = MongoClient(os.getenv('DB_LINK'))
db = client[os.getenv('DB_NAME')]


def create_user(db, effective_user, chat_id):
    user = {
        'user_id': effective_user.id,
        'first_name': effective_user.first_name,
        'last_name': effective_user.last_name,
        'username': effective_user.username,
        'chat_id': chat_id,
    }
    db.users.insert_one(user)
    return user


def get_user(db, effective_user, chat_id):
    user = db.users.find_one({'user_id': effective_user.id})
    if not user:
        create_user(db, effective_user, chat_id)
    return user
