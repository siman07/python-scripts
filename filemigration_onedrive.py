import os
import shutil
import datetime

downloads_folder = os.path.expanduser("~/Downloads")
documents_folder = os.path.expanduser("~/Documents")
onedrive_folder = os.path.expanduser("~/OneDrive")

# Calculate the date threshold
threshold_date = datetime.datetime.now() - datetime.timedelta(days=30)

def move_old_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # Get the file creation date
            file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            # Check if the file is older than the threshold date
            if file_creation_date < threshold_date:
                # Create the destination folder in OneDrive
                destination_folder = os.path.join(onedrive_folder, os.path.relpath(root, folder_path))
                os.makedirs(destination_folder, exist_ok=True)
                # Move the file to the destination folder
                shutil.move(file_path, destination_folder)
                print(f"Moved '{file_name}' to '{destination_folder}'")

# Move old files from Downloads folder
move_old_files(downloads_folder)

# Move old files from Documents folder
move_old_files(documents_folder)

