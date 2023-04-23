from threading import Thread
import glob
import os
import shutil
import re

main_path = input('Add path:')

extensions = {

    'video': ['mp4', 'mov', 'avi', 'mkv'],

    'audio': ['mp3', 'wav', 'ogg', "amr"],

    'image': ['jpg', 'png', 'jpeg', 'svg'],

    'archive': ['zip', 'gz', 'tar'],

    'documents': ['pdf', 'txt', 'doc', 'docx', 'xlsx', 'pptx'],

    "other": []
}


def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    return subfolder_paths


scripts = []


def recrusion(path, pat):
    if os.path.isfile(pat):
        file_path, file_name = os.path.split(pat)
        split_filename = file_name.split(".")
        scripts.append(split_filename[1])
        for key, value in extensions.items():
            if split_filename[1] in value:
                new_path = os.path.join(path, key)
                if not os.path.exists(os.path.join(path, key, file_name)):
                    shutil.move(pat, new_path)


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            os.rmdir(p)


if __name__ == "__main__":
    create_folders_from_list(main_path, extensions)

    threads = []
    for pat in glob.iglob(f'{main_path}/**/*', recursive=True):
        thread = Thread(target=recrusion, args=(main_path, pat, ))
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]

    remove_empty_folders(main_path)
