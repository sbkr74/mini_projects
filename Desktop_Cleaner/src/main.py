import os
import shutil
from pathlib import Path

def arrange_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path,filename)):
            # file_path = Path(filename)
            # file_ext = file_path.suffix
            file_ext = filename.split('.')[-1].lower()
            if file_ext:
                sub_folder = f"{file_ext.upper()}"
                if not os.path.isdir(sub_folder):
                    print("folder not created")
                else:
                    print("Already")

if __name__ == '__main__':
    folder_path = r"D:\downloads"
    if os.path.isdir(folder_path):
        arrange_folder(folder_path)
        print("Arrangement Done!!!")
    else:
        print("Invalid folder path.")