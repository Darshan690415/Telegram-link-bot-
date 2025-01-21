import os

def generate_direct_link(file_path):
    # Example: Upload file to your own server or third-party service
    base_url = "https://yourdomain.com/uploads"
    file_name = os.path.basename(file_path)
    return f"{base_url}/{file_name}"

def generate_streamable_link(file_id):
    # Example: Return a streaming link for videos
    return f"https://yourdomain.com/stream/{file_id}"