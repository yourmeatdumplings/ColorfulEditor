from json import dump
from src.Data.options_path.default import default_options

def create_options_file(fp):
    dump(default_options, fp, ensure_ascii=False, indent=4)