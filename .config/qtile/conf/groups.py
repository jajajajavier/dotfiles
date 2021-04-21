# Escritorios
#
# Qtile config groups por javier
# https://github.com/jajajajavier 


from conf.keys import mod, keys
from libqtile.config import Group, Key
from libqtile.lazy import lazy


groups = [Group(i) for i in [" ﲵ ", "  ", "  ", "   ", "  ", "  ", "  ", "  "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        
        # Cambiar  de Escritorio
        Key([mod], actual_key, lazy.group[group.name].toscreen()),

        # Mover ventana a otro escritorio 
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name, switch_group=True)),
])

