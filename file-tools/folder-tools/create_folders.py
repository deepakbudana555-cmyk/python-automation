  from pathlib import Path

folders = [
    "Projects",
    "Images",
    "Videos",
    "Documents",
    "Downloads"
]

for folder in folders:
    Path(folder).mkdir(exist_ok=True)

print("Folders created successfully.")
