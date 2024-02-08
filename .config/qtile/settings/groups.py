from libqtile.config import Group, EzKey
from libqtile.lazy import lazy
from .keys import keys

names = ["  ", " 󰈹 ", " 󰨞 ", " 󰈙 ", "  ", "  ", "  ", " 󰡨 ", "  "]
groups = [Group(i) for i in names]

for i in range(len(names)):
    key = str(i+1)
    keys.extend([
        EzKey("M-"+key, lazy.group[names[i]].toscreen()),
        EzKey("M-S-"+key, lazy.window.togroup(names[i]))
    ])
