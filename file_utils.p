import os
from config import MAX_FILE_SIZE_MB

def validate_file(file_size):
    # Check file size
    if file_size > MAX_FILE_SIZE_MB * 1024 * 1024:
        return False, f"File size exceeds {MAX_FILE_SIZE_MB} MB limit."
    return True, "File is valid."

def save_file_locally(file, upload_folder):
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, file.file_name)
    file.download(file_path)
    return file_path