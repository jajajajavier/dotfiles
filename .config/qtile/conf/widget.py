# Widgets config
#
# by javier
# https://github.com/jajajajavier


from libqtile    import widget
from conf.layout import colors


# >>>>>>>>>>|Elements|<<<<<<<<<<


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def Separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def Icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=5
    )

def ArrowL(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", 
        fontsize=37,
        padding=-5
    )

def ArrowR(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", 
        fontsize=37,
        padding=-5
    )

def Workspaces():
    return [
        Separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Hurmit Nerd Font',
            fontsize=20,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
            ),
]


# >>>>>>>>>>|Bar config|<<<<<<<<<<


widgets_1 = [
    
    # ----->Left part<-----
    
    # Q for Qtile XD
    Icon(
        bg='color3', 
        text='蘆',
        fontsize=20
        ), 

    ArrowR('color3', 'dark'),

    *Workspaces(),  

    Separator(),    

    # icon of windows orientation
    widget.CurrentLayoutIcon(
        **base(bg='color2'), 
        scale=0.65
        ),  
   
    # Name of windows orientation
    widget.CurrentLayout(
        **base(bg='color2'), 
        fontsize=14, 
        padding=5
        ),  

    ArrowR('color2','dark'),

    # Name of focus windows
    widget.WindowName(
        **base(fg='focus'), 
        fontsize=14, 
        padding=5
        ),  


    # ----->Right part<-----
    
    ArrowL('color3', 'dark'),

    ArrowL('dark', 'color3'),
    
    # Systray
    widget.Systray(     
        **base(bg='dark'), 
        Icon_size=20,
        padding=5
        ),

    Separator(),  

    ArrowL('color2', 'dark'),

    Icon(
        fg='dark', 
        bg='color2', 
        text='墳',
        fontsize=25 
        ),  
    
    # Volume percent %
    widget.Volume(
        **base(bg='color2'), 
        pading=5
        ), 

    ArrowL('color4', 'color2'),

    Icon(
        bg='color4', 
        fontsize=20, 
        text=''
        ),  

    # Batery percent and status
    widget.Battery(
        **base(bg='color4'),
        update_interval=5, 
        format='{percent:2.0%}{char}'
        ), 

    ArrowL('color1', 'color4'),

    Icon(
        bg='color1', 
        text='',
        fontsize=25
        ),    
    
    # CPU usage
    widget.CPU(     
        **base(bg='color1'), 
        format='{load_percent}% -'
        ),  

    Icon(
        bg='color1', 
        text='',
        fontsize=20
        ),  
    
    # RAM usage
    widget.Memory(      
        **base(bg='color1'), 
        format='{MemUsed:.0f}Mb'
        ),   

    ArrowL('color2', 'color1'),

    Icon(
        bg='color2', 
        text=' '
        ),   
    
    # Temperature in Celsius, I don't yanqui XD
    widget.OpenWeather(         #   for have local temperature visit: https://openweathermap.org/
        **base(bg='color2'),    #   search your city and open his info
        cityid='1234567',       #   look te numbers in the url : 
        format='{main_temp}°C'  #   https://openweathermap.org/city/[numbers]
        ),                      #   copy the numbers after /city/ and
                                #   paste in cityid: cityid='12345678',       
                                    
    ArrowL('dark', 'color2'),

    Icon(
        bg="dark", 
        fg='light', 
        fontsize=20, 
        text=' '),
    
    # Date and time
    widget.Clock(
        **base(fg='light', bg='dark'), 
        format='%d/%m/%Y - %H:%M '
        ),    
]

# Fonts, you need install this fonts
# installation with AUR helper:
# 
# nerd-fonts
# nerd-fonts-ubuntu-mono
# nerd-fonts-mononoki
# nerd-fonts-cascadia-cove
# nerd-fonts-hermit
# nerd-fonts-hack

widget_defaults = {
    # 'font': 'UbuntuMono Nerd Font',
    # 'font': 'Mononoki Nerd Font',
    # 'font': 'Caskaydia Cove Nerd Font',
    # 'font': 'Hack Nerd Font'
    'font': 'Hurmit Nerd Font', 
    'fontsize': 15,
    'padding': 5,
}

extension_defaults = widget_defaults.copy()
