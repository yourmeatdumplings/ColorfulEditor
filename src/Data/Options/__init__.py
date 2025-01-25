from os.path import exists
from typing import Any
from src.Data.Options.create import create_options_file
from src.Path import options_path
from json import load, dump
from src.Data.Options.default import default_options

global_options = {}

def init_options():
    if exists(options_path):
        check_options_integrity()
    else:
        with open(options_path, 'w', encoding='utf8') as fp:
            create_options_file(fp)

def check_options_integrity() -> None:
    global global_options

    read_options()

    for k, v in default_options.items():
        if not k in list(global_options.keys()):
            global_options[k] = v

    save_options()

def read_options() -> None:
    global global_options

    with open(options_path, 'r', encoding='utf-8') as f:
        s = load(f)
        global_options = s

def get_options(v: str) -> Any:
    global global_options

    for k, va in global_options.items():
        if k == v:
            s = global_options[k]
            return s

def save_options():
    global global_options

    with open(options_path, 'w', encoding='utf-8') as f:
        dump(global_options, f, indent=4, ensure_ascii=False)

def set_options(key: str, value: any) -> None:
    global global_options

    for k, v in global_options.items():
        if k == key:
            print(value)
            global_options[k] = value
            save_options()