from src.Data.Options import init_options
from src.Data.Package import init_package
from os import makedirs
from src.Path import projects_path, plugins_path

def init():
    makedirs(projects_path, exist_ok=True)
    makedirs(plugins_path, exist_ok=True)

    init_options()
    init_package()