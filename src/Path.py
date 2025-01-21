from os.path import dirname, realpath, join
from sys import argv

#base
base_path = dirname(realpath(argv[0]))

assets_path = join(base_path, 'Assets')

texture_2d_path = join(assets_path, 'Texture2D')

fonts_path = join(assets_path, 'Fonts')

default_font = join(fonts_path, 'default.ttf')