import os
import shutil

def create_subfolder(folder_path,sub_folder_name):
    sub_folder_path = os.path.join(folder_path,sub_folder_name)
    if not os.path.exists(sub_folder_path):
        os.makedirs(sub_folder_path)
    return sub_folder_path

def main(folder_path):
    if os.path.isdir(folder_path):
        for files in os.listdir(folder_path):
            file_path = os.path.join(folder_path,files)
            if os.path.isfile(file_path):
                file_ext = files.split(".")[-1]
                if file_ext:
                    sub_folder_name = file_ext.upper()
                    sub_folder_path = create_subfolder(folder_path,sub_folder_name)
                    new_loc = os.path.join(sub_folder_path,files)
                    if not os.path.exists(new_loc):
                        shutil.move(file_path,sub_folder_path)
                        print(f"Moved: {files} -> {sub_folder_name}")
                    else:
                        print(f"Skipped: {files} already exists in {sub_folder_name}")


if __name__=='__main__':
    folder_path = r'D:\desktop'
    main(folder_path)