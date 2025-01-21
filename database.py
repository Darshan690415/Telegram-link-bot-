import pymongo
from config import DB_URL

client = pymongo.MongoClient(DB_URL)
db = client["link_bot"]

def save_file(file_id, file_name, user_id, direct_link):
    db.files.insert_one({
        "file_id": file_id,
        "file_name": file_name,
        "user_id": user_id,
        "direct_link": direct_link
    })

def get_files_by_user(user_id):
    return db.files.find({"user_id": user_id})