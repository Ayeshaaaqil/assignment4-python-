
# Bulk File Re-namer Python Project/
# In this Code With Tomi tutorial, you will learn how to build a program that can go 
# into any folder on your computer and rename all of the files based on the conditions 
# set in your Python code.# import os

def bulk_rename(folder_path, prefix="", extension=""):
    """Renames all files in a folder with an optional prefix and extension change."""
    
    try:
        files = os.listdir(folder_path)  # Get all files in the directory
        for index, file in enumerate(files):
            old_path = os.path.join(folder_path, file)
            
            if os.path.isfile(old_path):  # Ensure it's a file, not a folder
                file_name, file_ext = os.path.splitext(file)  # Extract name and extension
                
                new_name = f"{prefix}{index + 1}{extension or file_ext}"
                new_path = os.path.join(folder_path, new_name)
                
                os.rename(old_path, new_path)  # Rename the file
                
        print("✅ Bulk renaming completed successfully!")
    
    except Exception as e:
        print(f"❌ Error: {e}")

# Example Usage:
folder = r"C:\Users\LENOVO\Desktop\TestFolder"  # Change this path
bulk_rename(folder, prefix="File_", extension=".txt")
