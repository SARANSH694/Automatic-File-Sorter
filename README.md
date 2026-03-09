# Automatic File Sorter

A Python utility that automatically organizes files into categorized folders based on file type and extension.

## Features

- **Automatic File Organization**: Sorts files into Images, Documents, Videos, Music, and Others folders
- **Scheduled Execution**: Runs daily at a specified time (default: 2:00 PM)
- **Cross-Platform Support**: Works on Windows, macOS, and Linux
- **Safe Operations**: Skips directories and avoids overwriting existing files
- **Error Handling**: Graceful error handling for failed operations

## File Categories

- **Images**: .jpg, .jpeg, .png, .gif
- **Documents**: .pdf, .docx, .txt
- **Videos**: .mp4, .avi, .mkv
- **Music**: .mp3, .wav, .flac
- **Others**: All other file types

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SARANSH694/Automatic-File-Sorter.git
   cd Automatic-File-Sorter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Update the path in the script to point to your target folder:
   ```python
   path = os.path.expanduser("~/Desktop/FolderA/")  # Edit this line
   ```

2. Run the script:
   ```bash
   python "Automatic File Sorter.py"
   ```

3. The script will start and run daily at 14:00 (2:00 PM). Keep the script running in the background.

## Configuration

Edit the scheduling time in the script:
```python
schedule.every().day.at("14:00").do(sort_files)  # Change "14:00" to your preferred time
```

## Requirements

- Python 3.6+
- schedule library

## How It Works

1. The script scans the specified directory
2. Creates category folders if they don't exist
3. Moves files to appropriate folders based on extension
4. Logs each operation
5. Skips nested directories and existing files

## Safety Features

- Files are never overwritten
- Directories are never moved
- Errors are caught and reported
- Original files are moved (not copied)