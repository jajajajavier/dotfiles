# Layout config
#
# by javier
# https://github.com/jajajajavier

import json
from libqtile        import layout 
from libqtile.config import Match

# Colors
with open('.config/qtile/settings/theme.json') as f:
    colors = json.load(f)


# Config of WIndows orientation
layout_conf = {
    "border_focus" : colors["focus"][0],
    "border_width" : 1,
    "margin" : 6,
    }

# Treetab orientation config
treetab_conf = {
        "font" : "Caskaydia Cove Nerd Font",
        "fontsize" : 10,
        "sections" : [""],
        "section_fontsize" : 10,
        "border_width" : 2,
        "bg_color" : colors['background'],
        "active_bg" : colors['focus'],
        "active_fg" : colors['background'],
        "inactive_bg" : colors['inactive'],
        "inactive_fg" : colors['background'],
        "padding_left" : 0,
        "padding_x" : 0,
        "padding_y" : 5,
        "section_top" : 10,
        "section_bottom" : 20,
        "level_shift" : 8,
        "vspace" : 3,
        "panel_width" : 150
}

# Orientations actives
layouts = [
    # layout.Matrix(**layout_conf),    
    # layout.Stack(num_stacks=2),
    # layout.Zoomy(**layout_conf),
    # layout.Tile(**layout_conf),
    layout.MonadTall(**layout_conf),
    layout.Columns(**layout_conf),
    layout.Max(),
    layout.RatioTile(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.VerticalTile(**layout_conf),
    layout.TreeTab(**treetab_conf),
]

# Config of floating windows
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
