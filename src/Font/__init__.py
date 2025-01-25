from src.Path import fonts_path
from os import walk

class Font:
    def __init__(self):
        self.src = ...


    @staticmethod
    def get_all_font():
        lst = []

        for paths, folders, files in walk(fonts_path):
            for file in files:
                if file.endswith('.ttf'):
                    lst.append(file.split('.')[0])

        return lst

    @property
    def path(self):
        return