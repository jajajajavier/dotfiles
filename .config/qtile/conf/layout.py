# Layout config
#
# por javier
# https://github.com/jajajajavier

from libqtile import layout 
from libqtile.config import Match
from conf.theme import colors


# Configuracion de las orientaciones de ventanas
layout_conf = {
    "border_focus" : colors["focus"][0],    # Color del borde 
    "border_width" : 1, # Tamaño del borde por pixeles
    "margin" : 6,   # Tamaño del espacio entre ventanas por pixeles
    }

# Configuracion solo del formato treetab
treetab_conf = {
        "font" : "Caskaydia Cove Nerd Font",
        "fontsize" : 10,
        "sections" : ["TABS"],
        "section_fontsize" : 10,
        "border_width" : 2,
        "bg_color" : "1c1f24",
        "active_bg" : "c678dd",
        "active_fg" : "000000",
        "inactive_bg" : "a9a1e1",
        "inactive_fg" : "1c1f24",
        "padding_left" : 0,
        "padding_x" : 0,
        "padding_y" : 5,
        "section_top" : 10,
        "section_bottom" : 20,
        "level_shift" : 8,
        "vspace" : 3,
        "panel_width" : 150
}

# Distribuciones activas
layouts = [
    # Para agregar o quitar solo descomentar o comentar :)
    #
    # layout.Matrix(**layout_conf),    
    # layout.Stack(num_stacks=2),
    # layout.Zoomy(**layout_conf),
    # layout.MonadTall(**layout_conf),
    layout.Columns(**layout_conf),
    layout.Max(),
    layout.Tile(**layout_conf),
    layout.RatioTile(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.VerticalTile(**layout_conf),
    layout.TreeTab(**treetab_conf),
]

# Configuracion de las ventanas flotantes
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        ],
    border_focus= colors["focus"][0],
    border_width= 1,
)
