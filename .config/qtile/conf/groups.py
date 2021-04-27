# Escritorios
#
# Qtile config groups por javier
# https://github.com/jajajajavier 


from conf.keys import mod, keys
from libqtile.config import Group, Key
from libqtile.lazy import lazy


# Para agregar o quitar iconos ir a https://www.nerdfonts.com/cheat-sheet,
# en el puedes encontrar bastantes iconos para remplazarlos por los mios
#
# Primero debes tener intaladas las nerd fonts de mi configuracion
# instalalas con un AUR helper: 
#
# nerd-fonts
# nerd-fonts-ubuntu-mono
# nerd-fonts-mononoki
# nerd-fonts-cascadia-code
# nerd-fonts-hermit

groups = [Group(i) for i in [" ﲵ ", "  ", "  ", "  ", "  ", "  ", "  ", "  ","  "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        
        # Cambiar  de Escritorio
        Key([mod], actual_key, lazy.group[group.name].toscreen()),

        # Mover ventana a otro escritorio 
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name, switch_group=True)),
])

# breve explicacion de los escritorios :
    #   ﲵ   =   Terminales
    #      =   Editor de texto
    #      =   Navegador
    #      =   Chat
    #      =   Juegos
    #      =   Musica
    #      =   Videos
    #      =   Cosas random, cualquier cosa, queria colocar un dado pero no pille XD
    #      =   Info del sistema, terminales con: administrador de recursos, un fetch, etc
