# Color Themes config
#
# https://github.com/jajajajavier
#
# parte 100% ctrl+c ctrl+v de archivo de configuracion de Antonio Sarosi
# https://github.com/antoniosarosi
# https://youtube.com/antoniosarosi


from os import path
import subprocess
import json

from conf.path import qtile_path


def load_theme():
    theme = "dark-grey"

    config = path.join(qtile_path, "config.json")
    if path.isfile(config):
        with open(config) as f:
            theme = json.load(f)["theme"]
    else:
        with open(config, "w") as f:
            f.write(f'{{"theme": "{theme}"}}\n')


    theme_file = path.join(qtile_path, "themes", f'{theme}.json')
    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as f:
        return json.load(f)


if __name__ == "conf.theme":
    colors = load_theme()
