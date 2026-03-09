import os
import shutil
import schedule
import time
from pathlib import Path

# Cross-platform path (works on Windows, macOS, Linux)
# For Windows: C:\Users\YourName\Desktop\FolderA\
# For macOS: /Users/YourName/Desktop/FolderA/
path = os.path.expanduser("~/Desktop/FolderA/")

# Ensure path exists
if not os.path.exists(path):
    print(f"Path does not exist: {path}")
    exit()

folder_names = ["Images", "Documents", "Videos", "Music", "Others"]

def sort_files():
    """Sort files into categorized folders"""
    try:
        # Create directories if they don't exist
        for folder in folder_names:
            folder_path = os.path.join(path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        
        # Get list of items in the directory
        file_list = os.listdir(path)
        
        for file in file_list:
            file_path = os.path.join(path, file)
            
            # Skip directories - only move files
            if not os.path.isfile(file_path):
                print(f"Skipping directory: {file}")
                continue
            
            # Skip if it already exists in destination
            destination = None
            
            if file.endswith((".jpg", ".jpeg", ".png", ".gif")):
                destination = os.path.join(path, "Images", file)
            elif file.endswith((".pdf", ".docx", ".txt")):
                destination = os.path.join(path, "Documents", file)
            elif file.endswith((".mp4", ".avi", ".mkv")):
                destination = os.path.join(path, "Videos", file)
            elif file.endswith((".mp3", ".wav", ".flac")):
                destination = os.path.join(path, "Music", file)
            else:
                destination = os.path.join(path, "Others", file)
            
            # Check if file already exists at destination
            if os.path.exists(destination):
                print(f"File already exists (skipped): {file}")
                continue
            
            # Move the file
            try:
                shutil.move(file_path, destination)
                print(f"Moved: {file} -> {destination}")
            except Exception as e:
                print(f"Error moving {file}: {e}")
    
    except Exception as e:
        print(f"Error in sort_files: {e}")

# Schedule the task to run daily at a specific time (e.g., 2:00 PM)
schedule.every().day.at("14:00").do(sort_files)

print("File sorter scheduled! Running at 14:00 (2:00 PM) daily.")
print("Keep this script running in the background.\n")

# Keep the scheduler running
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute if a task is due