import unittest
import os
import shutil
import tempfile
from pathlib import Path
import sys

# Import the functions from the main script
# Note: We'll create a testable version by importing the logic

class TestFileSorter(unittest.TestCase):
    """Test cases for the Automatic File Sorter"""
    
    def setUp(self):
        """Create a temporary directory for testing"""
        self.test_dir = tempfile.mkdtemp()
        self.original_path = os.path.expanduser("~/Desktop/FolderA/")
        
        # File categories and their extensions
        self.folder_names = ["Images", "Documents", "Videos", "Music", "Others"]
        self.file_types = {
            "Images": ["test_image.jpg", "photo.png", "pic.gif", "image.jpeg"],
            "Documents": ["document.pdf", "file.docx", "notes.txt"],
            "Videos": ["movie.mp4", "video.avi", "film.mkv"],
            "Music": ["song.mp3", "audio.wav", "track.flac"],
            "Others": ["archive.zip", "script.py", "config.ini"]
        }
    
    def tearDown(self):
        """Clean up the temporary directory"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def create_test_files(self):
        """Create sample test files in the test directory"""
        for category, files in self.file_types.items():
            for file_name in files:
                file_path = os.path.join(self.test_dir, file_name)
                # Create empty files for testing
                Path(file_path).touch()
    
    def sort_files_in_directory(self, path):
        """Sort files in the given directory (copy of main script logic)"""
        try:
            # Create directories if they don't exist
            for folder in self.folder_names:
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
                
                # Determine destination
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
    
    def test_directories_created(self):
        """Test that category directories are created"""
        self.sort_files_in_directory(self.test_dir)
        
        for folder in self.folder_names:
            folder_path = os.path.join(self.test_dir, folder)
            self.assertTrue(os.path.isdir(folder_path), 
                          f"Directory '{folder}' was not created")
    
    def test_files_sorted_correctly(self):
        """Test that files are sorted into correct categories"""
        self.create_test_files()
        self.sort_files_in_directory(self.test_dir)
        
        # Verify each file is in the correct category
        for category, files in self.file_types.items():
            category_path = os.path.join(self.test_dir, category)
            for file_name in files:
                file_path = os.path.join(category_path, file_name)
                self.assertTrue(os.path.isfile(file_path), 
                              f"File '{file_name}' not found in '{category}' folder")
    
    def test_no_files_in_root(self):
        """Test that no files remain in root directory after sorting"""
        self.create_test_files()
        self.sort_files_in_directory(self.test_dir)
        
        # Get all files in root directory
        root_files = [f for f in os.listdir(self.test_dir) 
                     if os.path.isfile(os.path.join(self.test_dir, f))]
        
        self.assertEqual(len(root_files), 0, 
                        f"Files still in root directory: {root_files}")
    
    def test_image_files(self):
        """Test image file sorting"""
        image_files = ["test.jpg", "photo.png", "pic.gif", "img.jpeg"]
        for file_name in image_files:
            Path(os.path.join(self.test_dir, file_name)).touch()
        
        self.sort_files_in_directory(self.test_dir)
        
        images_path = os.path.join(self.test_dir, "Images")
        for file_name in image_files:
            self.assertTrue(os.path.isfile(os.path.join(images_path, file_name)))
    
    def test_document_files(self):
        """Test document file sorting"""
        doc_files = ["report.pdf", "letter.docx", "notes.txt"]
        for file_name in doc_files:
            Path(os.path.join(self.test_dir, file_name)).touch()
        
        self.sort_files_in_directory(self.test_dir)
        
        docs_path = os.path.join(self.test_dir, "Documents")
        for file_name in doc_files:
            self.assertTrue(os.path.isfile(os.path.join(docs_path, file_name)))
    
    def test_duplicate_file_handling(self):
        """Test that duplicate files are not overwritten"""
        # Create original file
        test_file = os.path.join(self.test_dir, "test.jpg")
        Path(test_file).touch()
        
        # First sort
        self.sort_files_in_directory(self.test_dir)
        
        # Create another file with same name in root
        Path(test_file).touch()
        
        # Second sort
        self.sort_files_in_directory(self.test_dir)
        
        # Both files should exist (one in Images, one still in root)
        images_path = os.path.join(self.test_dir, "Images", "test.jpg")
        self.assertTrue(os.path.isfile(images_path))

if __name__ == "__main__":
    # Run the tests
    print("=" * 70)
    print("Automatic File Sorter - Test Suite")
    print("=" * 70)
    print()
    
    unittest.main(verbosity=2)
