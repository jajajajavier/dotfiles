# Qtile config por javier 
# https://github.com/jajajajavier
#
# archivo de configuracion default: 
# http://qtile.org
#
# hecho en arch linux 

# -------------------|Imports|--------------------

from libqtile import hook
from os import path
import os
import re
import socket
import subprocess

# ---------------|Config imports|--------------- 

from conf.keys import mod, keys, mouse
from conf.groups import groups
from conf.layout import layouts, floating_layout
from conf.widget import widget_defaults, extension_defaults
from conf.screen import screens
from conf.path import qtile_path

# ------------------------------------------------


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"

# Este archivo de configuracion se hizo con la info de la documentacion de Qtile
# para todas las veces que la "cage" en algo me ayudo mucho ver los archivos de
# Derek Taylor tiene un canal de youtube 100% recomendado, y el archivo  de configuracion 
# de Antonio Sarosi, tambien con un canal en youtube.
#
# CREDITOS=
#
# Derek Taylor ( Distro Tube) :
#   Youtube: https://youtube.com/distrotube
#   Gitlab: https://gitlab.com/dwt1
#
# Antonio Sarosi : 
#   youtube: https://youtube.com/antoniosarosi
#   Github: https://github.com/antoniosarosi
#
# Pasate por sus canales no seas puto
