# Widgets config
#
# by javier
# https://github.com/jajajajavier

from libqtile        import widget
from settings.layout import colors

# >>>>>>>>>>|Elements|<<<<<<<<<<

def base(fg='foreground', bg='background'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def Separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def Icon(fg='foreground', bg='background', fontsize=18, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=5
    )

def ArrowL(fg="foreground", bg="background"):
    return widget.TextBox(
        **base(fg, bg),
        text="", 
        fontsize=35,
        padding=-4
    )

def ArrowR(fg="foreground", bg="background"):
    return widget.TextBox(
        **base(fg, bg),
        text="", 
        fontsize=35,
        padding=-4
    )

def Workspaces():
    return [
        widget.GroupBox(
            **base(fg='foreground'),
            font='Hurmit Nerd Font',
            fontsize=20,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['foreground'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['orange'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['focus'],
            other_current_screen_border=colors['focus'],
            other_screen_border=colors['focus'],
            disable_drag=True
            ),
        ]

# >>>>>>>>>>|Bar config|<<<<<<<<<<
MyBar = [
    # ----->Left part<-----
    
    # Q for Qtile XD
    Icon(
        bg='magneta',
        fg='background',
        text='蘆',
        fontsize=20
        ), 

    ArrowR(
        fg='magneta',
        bg='background'
        ),

    Separator(),

    *Workspaces(),  

    Separator(),    

    # icon of windows orientation
    widget.CurrentLayoutIcon(
        **base(
            bg='focus', 
            fg='background'), 
        scale=0.65
        ),  
   
    # Name of windows orientation
    widget.CurrentLayout(
        **base(
            bg='focus', 
            fg='background'), 
        fontsize=14, 
        padding=5
        ),  

    ArrowR(
        fg='focus',
        bg='magneta',
        ),

    ArrowR(
        fg='magneta'),

    Separator(),

    # Name of focus windows
    widget.WindowName(
        **base(
            fg='magneta'), 
        fontsize=14, 
        padding=5
        ),  


    # ----->Right part<-----
    
    ArrowL(
        fg='magneta'
        ),

    ArrowL(
        fg='background',
        bg='magneta'
        ),

    # Systray
    widget.Systray(     
        **base(), 
        Icon_size=20,
        padding=5
        ),

    Separator(),  

    ArrowL(
        fg='yellow'
        ),

    Icon(
        bg='yellow',
        fg='background',
        text=''
        ),

    widget.CheckUpdates(
        **base(bg='yellow'),
        colour_have_updates=colors['background'],
        colour_no_updates=colors['background'], 
        no_update_string='0',
        display_format='{updates}',
        execute='alacritty -e paru -Syu',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    ArrowL(
        fg='orange',
        bg='yellow'
        ),

    Icon(
        bg='orange',
        fg='background',
        text='墳',
        fontsize=25 
        ),  
    
    # Volume percent %
    widget.Volume(
        **base(
            bg='orange', 
            fg='background'), 
        pading=5
        ), 

    ArrowL(
        fg='red',
        bg='orange'
        ),

    Icon(
        bg='red',
        fg='background',
        fontsize=20, 
        text=''
        ),  

    # Batery percent and status
    widget.Battery(
        **base(
            bg='red', 
            fg='background'),
        update_interval=5, 
        format='{percent:2.0%}{char}'
        ), 

    ArrowL(
        fg='magneta',
        bg='red'
        ),

    Icon(
        bg='magneta',
        fg='background',
        fontsize=20, 
        text=' '),
    
    # Date and time
    widget.Clock(
        **base(
            bg='magneta', 
            fg='background'), 
        format='%d/%m/%Y - %H:%M '
        ),    

    ArrowL(
        fg='background',
        bg='magneta'
        ),

    Icon(
        fg='blue',
        text=' '
        ),
]

# Fonts, you need install this font
# installation with AUR helper:
# 
# nerd-fonts-hack

widget_defaults = {
    'font': 'Hack Nerd Font', 
    'fontsize': 15,
    'padding': 5,
}

extension_defaults = widget_defaults.copy()
