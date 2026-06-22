import os
import shutil

source = "path/to/your/folder"
destination_base = "path/to/destination"

file_types = {
    ".jpg": "photos",
    ".png": "photos",
    ".pdf": "documents",
    ".docx": "documents",
    ".mp4": "videos",
    ".mp3": "music",
    ".zip": "archive"
}

for dirpath, dirnames, filenames in os.walk(source):
    for file in filenames:
        name, ext = os.path.splitext(file)
        
        if ext in file_types:
            folder_name = file_types[ext]
            destination = os.path.join(destination_base, folder_name)
            os.makedirs(destination, exist_ok=True)
            full_path = os.path.join(dirpath, file)
            shutil.move(full_path, destination)
            print(f"Moved {file} to {folder_name}")