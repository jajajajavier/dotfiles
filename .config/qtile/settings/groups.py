# Groups config
#
# by javier
# https://github.com/jajajajavier 

from settings.keys   import Win, keys
from libqtile.config import Group, Key
from libqtile.lazy   import lazy

# First, you need the fonts of my configuration
# install with AUR helper:
#
# nerd-fonts
# nerd-fonts-ubuntu-mono
# nerd-fonts-mononoki
# nerd-fonts-cascadia-code
# nerd-fonts-hermit
# nerd-fonts-hack
#
# For change icon visit https://www.nerdfonts.com/cheat-sheet
# copy your icon and paste here

group_names = [(" ﲵ ", {'layout': 'monadtall'}),    # Terminals
               ("  ", {'layout': 'ratiotile'}),    # Text editor
               ("  ", {'layout': 'monadwide'}),    # Web Browser
               ("  ", {'layout': 'treetab'}),      # Chat
               ("  ", {'layout': 'max'}),          # Games
               ("  ", {'layout': 'bsp'}),          # File manager
               ("  ", {'layout': 'verticaltile'}), # Music
               ("  ", {'layout': 'max'}),          # Multimedia
               ("  ", {'layout': 'columns'})]      # Random

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.extend([
        # Change group
        Key([Win], str(i), lazy.group[name].toscreen(),         desc="Win + Number"),

        # Move windows to another group
        Key([Win, "shift"], str(i), lazy.window.togroup(name),  desc="Win + Shift + Number")
        ])


    








