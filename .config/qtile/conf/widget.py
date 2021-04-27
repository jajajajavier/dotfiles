# Widgets
#
# config por javier
# https://github.com/jajajajavier


from libqtile import widget
from conf.theme import colors
from libqtile import qtile
from libqtile.config import Click
from libqtile.lazy import lazy
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
        padding=3
    )

def flecha_L(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-5
    )

def flecha_R(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_right
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


# >>>>>>>>>>|Barra Configuracion|<<<<<<<<<<


# Colores:
#   light:  Blanco
#   dark:   Fondo de la barra
#   color1: Rojo
#   color2: Morado
#   color3: Azul
#   color4: Amarillo

widgets_1 = [
    
    # ----->Parte izquierda<-----
    
    icono(bg='color3', text='蘆'), 

    flecha_R('color3', 'dark'),

    *Escritorios(),  

    separador(),    

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),  
   
    widget.CurrentLayout(**base(bg='color2'), fontsize=14,padding=5),  

    flecha_R('color2','dark'),

    widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),  


    # ----->Parte derecha<-----
    
    flecha_L('color3', 'dark'),

    flecha_L('dark', 'color3'),

    widget.Systray(background=colors['dark'], padding=5),   # Bandeja del Sistema

    separador(),  

    flecha_L('color2', 'dark'),

    icono(fg='dark', bg='color2', text=' '),  
    
    widget.Volume(**base(bg='color2'), pading=5), 

    flecha_L('color4', 'color2'),

    icono(bg='color4', text=''),  

    widget.Battery(**base(bg='color4'), update_interval=5, format='{percent:2.0%}{char}'), 

    flecha_L('color1', 'color4'),

    icono(bg='color1', text=''),    

    widget.CPU(**base(bg='color1'), format='{load_percent}%'),  # Consumo de la CPU

    icono(bg='color1', text='- '),  

    widget.Memory(**base(bg='color1'), format='{MemUsed:.0f}Mb'),   # Consumo de RAM

    flecha_L('color2', 'color1'),

    icono(bg='color2', text=' '),   

    widget.OpenWeather(**base(bg='color2'), cityid='xdxdxd', format='{main_temp}°C'),  # Temperatura en °C
        #   Para tener tempertura local ir a https://openweathermap.org/ 
        #   buscar tu ciudad o la mas cercana y metete a su info 
        #   ahora mira la url del sitio, deberia ser algo asi:
        #   https://openweathermap.org/city/[numeros]
        #   copia los numeros de la url y pegalos en cityid

    flecha_L('dark', 'color2'),

    icono(bg="dark", fg='light', fontsize=17, text=' '),

    widget.Clock(**base(fg='light', bg='dark'), format='%d/%m/%Y - %H:%M '),    # Fecha y Hora
]


widget_defaults = {
    # 'font': 'UbuntuMono Nerd Font',
    # 'font': 'Mononoki Nerd Font',
    # 'font': 'Caskaydia Cove Nerd Font',
    'font': 'Hurmit Nerd Font', 
    'fontsize': 15,
    'padding': 5,
}

extension_defaults = widget_defaults.copy()
