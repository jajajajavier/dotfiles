# Screens config
# 
# by javier
# https://github.com/jajajajavier


from libqtile.config import Screen
from libqtile import widget, bar
from conf.widget import widgets_1


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=1)


screens = [Screen(top=status_bar(widgets_1))]
