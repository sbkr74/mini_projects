import os
import shutil
from pathlib import Path

def create_subfolder(folder_path,sub_folder):
    sub_folder_path = os.path.join(folder_path,sub_folder)
    os.makedirs(sub_folder_path,exist_ok=True)
    return sub_folder_path

def arrange_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path,filename)):
            file_ext = filename.split('.')[-1].lower()
            if file_ext:
                sub_folder = file_ext.upper()
                sub_folder_path = os.path.join(folder_path,sub_folder)
                file_path = os.path.join(folder_path,filename)
                new_loc = os.path.join(sub_folder_path,file_path)
                if not os.path.isdir(sub_folder_path):
                    create_subfolder(folder_path,sub_folder)
                    print(sub_folder_path)
                if os.path.exists(new_loc):
                    shutil.move(file_path,sub_folder_path)
                    print('moved')

if __name__ == '__main__':
    folder_path = r"D:\downloads"
    if os.path.isdir(folder_path):
        arrange_folder(folder_path)
        print("Arrangement Done!!!")
    else:
        print("Invalid folder path.")