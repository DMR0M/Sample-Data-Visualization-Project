import os
import glob
import shutil


class FileManager:
    def __init__(self, target: str):
        self.paths = target.split('/')
        self.path = target
        self.folder = '/'.join(self.paths[:len(self.paths)-1])

    def display_content(self):
        try:
            with open(self.path, 'r', encoding='UTF8') as f:
                lines = f.readlines()
                for line in lines:
                    print(line, end=' ')
            return 'done'
        except FileNotFoundError:
            return 'file not found'
        except PermissionError:
            return 'target is not a file'

    def check_file_size(self):
        if not os.path.isfile(self.path):
            return 'target is not a file'
        try:
            print(os.stat(self.path))
            print(f'File size: {os.stat(self.path).st_size} bytes')
            return 'done'
        except FileNotFoundError:
            return 'file not found'

    def check_dir_size(self):
        if not os.path.isdir(self.path):
            return 'target is not a folder'
        try:
            print(os.stat(self.path))
            print(f'Folder size: {os.stat(self.path).st_size} bytes')
            return 'done'
        except FileNotFoundError:
            return 'directory not found'

    def copy_csv(self, folder):
        """Copy all csv files"""
        # Check if given arg exists, if not create directory
        if not os.path.exists(folder):
            os.mkdir(folder)

        csvs = glob.glob(f'{self.folder}/*.csv')
        for file in csvs:
            shutil.copy(file, folder)
        return 'done'

    def move_csv(self, folder):
        """Move all csv files"""
        # Check if given arg exists, if not create directory
        if not os.path.exists(folder):
            os.mkdir(folder)

        csvs = glob.glob(f'{self.folder}/*.csv')
        for file in csvs:
            shutil.move(file, folder)
        return 'done'


def main():
    path = '../../csv_data_2/pokemon.txt'
    fm = FileManager(path)
    print(fm.move_csv('../../backup_1/'))


if __name__ == '__main__':
    main()
