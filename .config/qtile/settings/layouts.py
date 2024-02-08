from libqtile import layout
from libqtile.config import Match
from .theme import theme

appearance = {
    'border_focus': theme['focus'],
    'border_width': 1,
    'margin': 5
}

layouts = [i(**appearance) for i in [
    layout.MonadTall,
    layout.MonadWide,
    layout.Columns,
    layout.Floating,
]]
layouts.append(layout.Max())

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=theme['focus']
)
