from libqtile.config import Screen
from .widgets import widgets
from libqtile import bar


screens = [
    Screen(
        wallpaper_mode='stretch', wallpaper='~/Pictures/2.png',
        top=bar.Bar(widgets, 24)
    )
]
