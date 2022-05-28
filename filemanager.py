import shutil
import os
import sys


def copy_file_or_directory(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copyfile(name, new_name)


def filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    return result

def save_filenames():
    result = {
        "files": [],
        "dirs": []
    }
    for item in os.listdir():
        if os.path.isfile(item):
            file = result["files"]
            file.append(item)
        else:
            dir = result["dirs"]
            dir.append(item)
    list_result = [f'{key}, {value}' for key, value in result.items()]
    return list_result

def author_info():
    return 'Leonid Orlov'


def quit():
    sys.exit(0)

if __name__ == '__main__':
    print(save_filenames())