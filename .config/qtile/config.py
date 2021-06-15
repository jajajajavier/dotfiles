# Qtile config 
# por javier 
# https://github.com/jajajajavier
#
# Default config: 
# http://qtile.org
#
# make in arch linux 

# ---------------|Settings imports|--------------- 

from settings.keys   import keys, mouse
from settings.groups import groups
from settings.layout import layouts, floating_layout
from settings.widget import widget_defaults, extension_defaults
from settings.screen import screens
# ------------------------------------------------

dgroups_key_binder = None
dgroups_app_rules = []
main = None 
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"

# This config file his made with the info of the qtile documentation,
# for all my mistakes, i watched the config file of Derek Taylor (english) and
# Antonio Sarosi (spanish). Thanks
#
# CREDITS=
#
# Derek Taylor ( Distro Tube) :
#   Youtube: https://youtube.com/distrotube
#   Gitlab: https://gitlab.com/dwt1
#
# Antonio Sarosi : 
#   youtube: https://youtube.com/antoniosarosi
#   Github: https://github.com/antoniosarosi
#
# see their chanels
