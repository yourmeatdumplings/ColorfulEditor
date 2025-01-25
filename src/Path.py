from os.path import dirname, realpath, join
from sys import argv

#base
base_path = dirname(realpath(argv[0]))

options_path = join(base_path, 'options.json')

package_path = join(base_path, 'package.json')

assets_path = join(base_path, 'Assets')

data_path = join(base_path, 'Data')

lang_path = join(base_path, 'Lang')

texture_2d_path = join(assets_path, 'Texture2D')

fonts_path = join(assets_path, 'Fonts')

projects_path = join(base_path, 'Projects')

plugins_path = join(base_path, 'Plugins')

default_font = join(fonts_path, 'JeTBrainsMono.ttf')