import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("25352517")
API_HASH = os.getenv("2b7e6cf7752c3af91f958d67793a3e0b")
BOT_TOKEN = os.getenv("7941063228:AAGlUgHUXgU3JYU1unjuFFiCSiwKLTbvpsE")
DB_URL = os.getenv("mongodb+srv://rstock937:57HBrMeNXnc2yFvx@cluster0.hte7t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # MongoDB or SQLite URL
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", 10000))  # File size limit
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "./uploads")
