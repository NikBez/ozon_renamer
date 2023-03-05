import os
from pathlib import Path


DEFAULT_PATH = '.'
SUFFIXES = ['.jpg', '.jpeg']


def main():
    folders = scan_dirs()
    for parent, folders_list in folders.items():
        for folder in folders_list:
            rename_files(folder)


def scan_dirs():
    folders = {}
    with os.scandir(DEFAULT_PATH) as parent_folders:
        parent_folders = [folder for folder in parent_folders if folder.is_dir() and folder.name not in ['.idea', '.git']]
    for folder in parent_folders:
        with os.scandir(folder.path) as pic_folders:
            folders[folder] = [pic_folder for pic_folder in pic_folders if pic_folder.is_dir()]
    return folders


def rename_files(folder):
    counter = 0
    files = os.scandir(folder.path)
    for file in sorted(files, key=lambda file: file.name):
        if Path(file).suffix.lower() in SUFFIXES:
            if not counter:
                os.rename(Path(file.path), Path(file.path).parents[0]/f'{folder.name}.jpg')
            else:
                os.rename(Path(file.path), Path(file.path).parents[0] / f'{folder.name}@{counter}.jpg')
            counter += 1


if __name__ == '__main__':
    main()
