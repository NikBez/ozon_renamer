import os
from pathlib import Path


DEFAULT_PATH = '.'
SUFFIX = '.jpg'


def main():
    folders = {}
    with os.scandir(DEFAULT_PATH) as parent_files:
        parent_folders = [file.name for file in parent_files if os.path.isdir(file) and file.name != '.idea']
        for folder in parent_folders:
            with os.scandir(Path(DEFAULT_PATH)/folder) as files:
                folders[folder] = [file.name for file in files if os.path.isdir(file) and file.name != '.idea']

    for parent, folders_list in folders.items():
        for folder in folders_list:
            counter = 0
            files = os.listdir(Path(DEFAULT_PATH) / parent / folder)
            for file in sorted(files, key=lambda file: file):
                ext = Path(file).SUFFIX
                if ext == SUFFIX:
                    if not counter:
                        os.rename(Path(DEFAULT_PATH) / parent / folder / file,
                                  Path(DEFAULT_PATH) / parent / folder / f'{folder}.jpg')
                    else:
                        os.rename(Path(DEFAULT_PATH) / parent / folder / file,
                                  Path(DEFAULT_PATH) / parent / folder / f'{folder}@{counter}.jpg')
                    counter += 1


if __name__ == '__main__':
    main()
