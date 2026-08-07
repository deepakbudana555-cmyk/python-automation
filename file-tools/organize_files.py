from pathlib import Path
import shutil

DOWNLOADS = Path.home() / "Downloads"

FILE_TYPES = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "PDF",
    ".mp4": "Videos",
    ".mp3": "Music",
    ".zip": "Archives",
    ".docx": "Documents",
    ".xlsx": "Documents",
}

for file in DOWNLOADS.iterdir():
    if file.is_file():
        folder = FILE_TYPES.get(file.suffix.lower())
        if folder:
            destination = DOWNLOADS / folder
            destination.mkdir(exist_ok=True)
            shutil.move(str(file), destination / file.name)

print("Files organized successfully.")
