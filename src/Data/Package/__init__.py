from os.path import exists
from typing import Any
from src.Data.Package.create import create_package_file
from src.Path import package_path
from json import load, dump
from src.Data.Package.default import default_package

global_package = {}

def init_package():
    if exists(package_path):
        check_package_integrity()
    else:
        with open(package_path, 'w', encoding='utf8') as fp:
            create_package_file(fp)

def check_package_integrity() -> None:
    global global_package

    read_package()

    for k, v in default_package.items():
        if not k in list(global_package.keys()):
            global_package[k] = v
        if k == 'version':
            global_package[k] = v
        if k == 'path':
            global_package[k] = v

    save_package()

def read_package() -> None:
    global global_package

    with open(package_path, 'r', encoding='utf-8') as f:
        s = load(f)
        global_package = s

def get_package(v: str) -> Any:
    global global_package

    for k, va in global_package.items():
        if k == v:
            s = global_package[k]
            return s

def save_package():
    global global_package

    with open(package_path, 'w', encoding='utf-8') as f:
        dump(global_package, f, indent=4, ensure_ascii=False)

def set_package(key: str, value: any) -> None:
    global global_package

    for k, v in global_package.items():
        if k == key:
            print(value)
            global_package[k] = value
            save_package()