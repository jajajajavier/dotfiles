# Groups config
#
# por javier
# https://github.com/jajajajavier 

from conf.keys import Win, keys
from libqtile.config import Group, Key
from libqtile.lazy import lazy

# Para agregar o quitar iconos ir a https://www.nerdfonts.com/cheat-sheet,
# en el puedes encontrar bastantes iconos para remplazarlos por los mios
#
# Primero debes tener instaladas las nerd fonts de mi configuracion
# debes instalarlas con un AUR helper: 
#
# nerd-fonts
# nerd-fonts-ubuntu-mono
# nerd-fonts-mononoki
# nerd-fonts-cascadia-code
# nerd-fonts-hermit
# nerd-fonts-hack

group_names = [(" ﲵ ", {'layout': 'monadtall'}),    # Terminales
               ("  ", {'layout': 'ratiotile'}),    # Editor de texto
               ("  ", {'layout': 'monadwide'}),    # Navegador web
               ("  ", {'layout': 'treetab'}),      # Chat
               ("  ", {'layout': 'max'}),          # Juegos
               ("  ", {'layout': 'bsp'}),          # Navegador de archivos, siempre viene bien :)
               ("  ", {'layout': 'verticaltile'}), # Musica
               ("  ", {'layout': 'max'}),          # Videos
               ("  ", {'layout': 'columns'})]      # Cosas random, cualquier cosa

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.extend([

        # Cambiar  de Escritorio
        Key([Win], str(i), lazy.group[name].toscreen()),

        # Mover ventana a otro escritorio 
        Key([Win, "shift"], str(i), lazy.window.togroup(name))])


    








