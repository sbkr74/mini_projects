import os
import shutil

def create_subfolder(parent_path, sub_folder_name):
    """Creates a subfolder if it doesn't exist and returns its path."""
    sub_folder_path = os.path.join(parent_path, sub_folder_name)
    os.makedirs(sub_folder_path, exist_ok=True)
    return sub_folder_path

def move_file(file_path, sub_folder_path, file_name):
    """Moves a file to the specified subfolder."""
    new_location = os.path.join(sub_folder_path, file_name)
    if not os.path.exists(new_location):
        shutil.move(file_path, sub_folder_path)
        print(f"Moved: {file_name} -> {sub_folder_path}")
    else:
        print(f"Skipped: {file_name} already exists in {sub_folder_path}")

def organize_files_by_extension(folder_path):
    """Organizes files in a folder by their extensions."""
    if not os.path.isdir(folder_path):
        print(f"Invalid directory: {folder_path}")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            file_ext = file_name.split(".")[-1]

            if file_ext:  # Ensure the file has an extension
                sub_folder_name = file_ext.upper()
                sub_folder_path = create_subfolder(folder_path, sub_folder_name)
                move_file(file_path, sub_folder_path, file_name)

   

if __name__ == '__main__':
    folder_path = r"D:\downloads"
    organize_files_by_extension(folder_path)