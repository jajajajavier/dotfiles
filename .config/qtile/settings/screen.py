# Screens config
# 
# by javier
# https://github.com/jajajajavier

from libqtile        import widget, bar
from libqtile.config import Screen
from settings.widget import MyBar


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=1)

screens = [Screen(top=status_bar(MyBar))]
