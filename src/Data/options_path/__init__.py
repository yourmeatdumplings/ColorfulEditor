from os.path import exists
from src.Data.options_path.create import create_options_file
from src.Path import options_path


def init_options():
    if exists(options_path):
        ...
    else:
        with open(options_path, 'w', encoding='utf8') as fp:
            create_options_file(fp)