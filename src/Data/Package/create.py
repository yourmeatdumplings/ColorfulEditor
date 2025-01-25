from json import dump
from src.Data.Package.default import default_package

def create_package_file(fp):
    dump(default_package, fp, ensure_ascii=False, indent=4)