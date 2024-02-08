from libqtile.config import EzKey, EzClick, EzDrag
from libqtile.lazy import lazy
from os import path

home = path.expanduser('~')
my_terminal = "alacritty"

keys = [EzKey(i[0], i[1]) for i in[
    # group functions
    ("M-<space>", lazy.next_layout()),
    ("M-S-<space>", lazy.prev_layout()),
    ("M-S-h", lazy.layout.swap_left()),
    ("M-S-l", lazy.layout.swap_right()),
    ("M-S-h", lazy.layout.shuffle_left()),
    ("M-S-j", lazy.layout.shuffle_down()),
    ("M-S-k", lazy.layout.shuffle_up()),
    ("M-S-l", lazy.layout.shuffle_right()),
    ("M-A-h", lazy.layout.swap_column_left()),
    ("M-A-l", lazy.layout.swap_column_right()),
    ("M-C-h", lazy.layout.grow_left()),
    ("M-C-j", lazy.layout.grow_down()),
    ("M-C-k", lazy.layout.grow_up()),
    ("M-C-l", lazy.layout.grow_right()),
    ("M-C-m", lazy.layout.maximize()),
    ("M-C-j", lazy.layout.shrink()),
    ("M-C-k", lazy.layout.grow()),
    ("M-C-n", lazy.layout.normalize()),
    ("M-A-h", lazy.layout.flip()),
    ("M-A-l", lazy.layout.flip()),

    # window functions
    ("M-w", lazy.window.kill()),
    ("M-<F11>", lazy.window.toggle_fullscreen()),
    ("M-t", lazy.window.toggle_floating()),
    ("M-<Tab>", lazy.group.next_window()),
    ("M-S-<Tab>", lazy.group.prev_window()),
    ("M-h", lazy.layout.left()),
    ("M-j", lazy.layout.down()),
    ("M-k", lazy.layout.up()),
    ("M-l", lazy.layout.right()),

    # qtile session
    ("M-C-r", lazy.restart()),
    ("M-C-q", lazy.shutdown()),

    # Brightness
    ("<XF86MonBrightnessDown>", lazy.spawn('brightnessctl s 5%-')),
    ("<XF86MonBrightnessUp>", lazy.spawn('brightnessctl s +5%')),


    # applications
    ("M-<return>", lazy.spawn(my_terminal)),
    ("M-d", lazy.spawn(home+"/.config/rofi/scripts/launcher_t2")),
    ("M-f", lazy.spawn("pcmanfm")),
]]

mouse = [
    EzDrag("M-1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    EzDrag("M-3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    EzClick("M-2", lazy.window.bring_to_front())
]
