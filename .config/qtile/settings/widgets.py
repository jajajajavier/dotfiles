from libqtile import widget
from .theme import theme

widget_defaults = {
    'font':     'JetBrainsMonoNF',
    'fontsize': 14,
    'padding':  0,
}
extension_defaults = widget_defaults

def colors(bg='dark', fg='text'):
    return {
        'background': theme[bg],
        'foreground': theme[fg],
    }

def arrow_r(bg='dark', fg='light'):
    return widget.TextBox(
        **colors(bg, fg),
        text=" ",
        fontsize=34, 
        margin_x=0,
        margin_y=0,
        padding=-8,
    ),

def arrow_l(bg='dark', fg='light'):
    return widget.TextBox(
        **colors(bg, fg),
        text="",
        fontsize=34, 
        margin_x=0,
        margin_y=0,
        padding=-2,
    ),

def icon(text='?', bg='dark', fg='text', fontsize=22):
    return widget.TextBox(
        **colors(bg, fg),
        text=text,
        fontsize=fontsize,
        padding=6,
        ),

def separator(bg='dark', pad=6):
    return widget.Sep(
        **colors(bg, bg),
        padding=pad
    ),

def groups():
    return widget.GroupBox(
        **colors(fg='light'),
        fontsize=20,
        margin_y=2,
        margin_x=0,
        padding_y=0,
        padding_x=5,
        borderwidth=1,
        active=theme['active'],
        inactive=theme['inactive'],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=theme['urgent'],
        this_current_screen_border=theme['focus'],
        this_screen_border=theme['grey'],
        other_current_screen_border=theme['dark'],
        other_screen_border=theme['dark'],
        disable_drag=True
        ),

widgets = [
    *groups(),
    *separator(),
    *separator('text'),
    widget.CurrentLayoutIcon(**colors(bg='text')),
    *separator('text'),
    widget.CurrentLayout(**colors(bg='text', fg='light')),
    *arrow_r(fg='text'),
    widget.WindowName(**colors(fg='green')),

    *icon('', fg='magenta', fontsize=35),
    widget.Systray(**colors()),
    *arrow_l(fg='red'),
    *icon('', 'red'),
    widget.ThermalSensor(**colors(bg='red')),
    *arrow_l('red', 'magenta'),
    *icon(' ', 'magenta'),
    widget.Memory(**colors(bg='magenta')),
    *arrow_l('magenta', 'blue'),
    *icon(' ', 'blue'),
    widget.CPU(
        **colors(bg='blue'),
        format='{freq_current}GHz {load_percent}%',
        ),
    *arrow_l('blue', 'green'),
    *icon(' ', 'green'),
    widget.Clock(**colors(bg='green')),
    *separator('green', 12),
]

