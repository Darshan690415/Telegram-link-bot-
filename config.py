import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_URL = os.getenv("mongodb+srv://rstock937:57HBrMeNXnc2yFvx@cluster0.hte7t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # MongoDB or SQLite URL
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", 50))  # File size limit
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "./uploads")
