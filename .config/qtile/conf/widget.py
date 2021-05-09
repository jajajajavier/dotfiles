# Widgets confi
#
# Por javier
# https://github.com/jajajajavier


from libqtile import widget
from conf.theme import colors
from libqtile import qtile


# >>>>>>>>>>|Elementos|<<<<<<<<<<


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separador():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icono(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=5
    )

def flecha_L(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", 
        fontsize=37,
        padding=-5
    )

def flecha_R(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", 
        fontsize=37,
        padding=-5
    )

def Escritorios():
    return [
        separador(),
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


# >>>>>>>>>>|Configuracion de la barra|<<<<<<<<<<


widgets_1 = [
    
    # ----->Parte izquierda<-----
    
    # Solo una q por Qtile XD
    icono(
        bg='color3', 
        text='蘆',
        fontsize=20
        ), 

    flecha_R('color3', 'dark'),

    *Escritorios(),  

    separador(),    

    # Icono distribucion de ventanas
    widget.CurrentLayoutIcon(
        **base(bg='color2'), 
        scale=0.65
        ),  
   
    # Distribucion de ventanas
    widget.CurrentLayout(
        **base(bg='color2'), 
        fontsize=14, 
        padding=5
        ),  

    flecha_R('color2','dark'),

    # Nombre ventana enfocada
    widget.WindowName(
        **base(fg='focus'), 
        fontsize=14, 
        padding=5
        ),  


    # ----->Parte derecha<-----
    
    flecha_L('color3', 'dark'),

    flecha_L('dark', 'color3'),
    
    # Bandeja del sistema
    widget.Systray(     
        **base(bg='dark'), 
        icon_size=22,
        padding=5
        ),

    separador(),  

    flecha_L('color2', 'dark'),

    icono(
        fg='dark', 
        bg='color2', 
        text='墳',
        fontsize=25 
        ),  
    
    # Indicador de volumen %
    widget.Volume(
        **base(bg='color2'), 
        pading=5
        ), 

    flecha_L('color4', 'color2'),

    icono(
        bg='color4', 
        fontsize=20, 
        text=''
        ),  

    # Porceentaje de bateria 
    widget.Battery(
        **base(bg='color4'),
        update_interval=5, 
        format='{percent:2.0%}{char}'
        ), 

    flecha_L('color1', 'color4'),

    icono(
        bg='color1', 
        text='',
        fontsize=25
        ),    
    
    # Consumo de la CPU
    widget.CPU(     
        **base(bg='color1'), 
        format='{load_percent}% -'
        ),  

    icono(
        bg='color1', 
        text='',
        fontsize=20
        ),  
    
    # Consumo de RAM
    widget.Memory(      
        **base(bg='color1'), 
        format='{MemUsed:.0f}Mb'
        ),   

    flecha_L('color2', 'color1'),

    icono(
        bg='color2', 
        text=' '
        ),   
    
    # Temperatura de tu ciudad en °C
    widget.OpenWeather(         #   Para tener tempertura local ir a https://openweathermap.org/
        **base(bg='color2'),    #   buscar tu ciudad o la mas cercana y entra a su info
        cityid='numeros',       #   ahora mira la url del sitio deberia ser algo asi: 
        format='{main_temp}°C'  #   https://openweathermap.org/city/[numeros]
        ),                      #   copia los numeros que vienen despues de /city/ en la url y
                                #   pegalos en cityid de tal manera: cityid='12345678',       
                                    
    flecha_L('dark', 'color2'),

    icono(
        bg="dark", 
        fg='light', 
        fontsize=20, 
        text=' '),
    
    # Fecha y Hora
    widget.Clock(
        **base(fg='light', bg='dark'), 
        format='%d/%m/%Y - %H:%M '
        ),    
]

# Configuracion de la fuente.
# instalala las fuentes con un AUR helper:
# 
# nerd-fonts
# nerd-fonts-ubuntu-mono
# nerd-fonts-mononoki
# nerd-fonts-cascadia-cove
# nerd-fonts-hermit

widget_defaults = {
    # 'font': 'UbuntuMono Nerd Font',
    # 'font': 'Mononoki Nerd Font',
    # 'font': 'Caskaydia Cove Nerd Font',
    'font': 'Hurmit Nerd Font', 
    'fontsize': 15,
    'padding': 5,
}

extension_defaults = widget_defaults.copy()
