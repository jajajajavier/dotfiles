# Widgets
#
# config por javier
# https://github.com/jajajajavier


from libqtile import widget
from conf.theme import colors


# >>>>>>>>>>|Elementos|<<<<<<<<<<


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=16, text="?"):
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

def workspaces():
    return [
        separator(),
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

primary_widgets = [
    
    # ----->Parte izquierda<-----
    
    icon(bg='color3', text='蘆'),   # Solo es una Q por Qtile XD

    flecha_R('color3', 'dark'),     # Flecha color azul fondo dark

    *workspaces(),  # Escritorios

    separator(),    # Un separador entre los escritorios y el formato de ventanas

    flecha_R('dark','color2'),  # Flecha color Dark fondo morado

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),  # Icono de distibucion de las ventanas

    widget.CurrentLayout(**base(bg='color2'), fontsize=14,padding=5),   # Formato de ventanas

    flecha_R('color2','dark'),  # Flecha morada fondo dark

    widget.WindowName(**base(fg='focus'), fontsize=16, padding=5),  # Nombre de la ventana enfocada


    # ----->Parte derecha<-----
    
    flecha_L('color3', 'dark'),

    flecha_L('dark', 'color3'),

    widget.Systray(background=colors['dark'], padding=5),   # Bandeja del Sistema

    separator(),    # Un separador para que la Bandeja del sistema no quede muy pegado con el volumen

    flecha_L('color2', 'dark'),

    icon(fg='dark', bg='color2', text=' '),    # Icono de volumen
    
    widget.Volume(**base(bg='color2'), pading=5),   # Porcentaje de volumen

    flecha_L('color4', 'color2'),

    icon(bg='color4', text=''),    # Icono de bateria

    widget.Battery(**base(bg='color4'), update_interval=5, format='{percent:2.0%}{char}'),  # Porcentaje de bateria

    flecha_L('color3', 'color4'),

    icon(bg="color3", text=' '),   # Icono de internet

    widget.Net(**base(bg='color3'), interface='wlp2s0', format='{down}  {up}'),   # velocidad de internet

    flecha_L('color1', 'color3'),

    icon(bg='color1', text=''),    # Icono de CPU

    widget.CPU(**base(bg='color1'), format='{load_percent}%'),  # Consumo de la CPU

    icon(bg='color1', text='- '),  # Icono de memoria RAM

    widget.Memory(**base(bg='color1'), format='{MemUsed:.0f}Mb'),   # Consumo de RAM

    flecha_L('color2', 'color1'),

    icon(bg='color2', text=' '),   # Icono de Tiempo

    widget.OpenWeather(**base(bg='color2'), cityid='3882582', format='{main_temp}°C'),  # Temperatura en °C
        #   Para tener temperatura local ir a https://openweathermap.org/ 
        #   buscar tu ciudad o la mas cercana y metete a su info 
        #   ahora mira la url del sitio, deberia ser algo asi:
        #   https://openweathermap.org/city/[numeros]
        #   copia los numeros de la url y pegalos en cityid

    flecha_L('dark', 'color2'),

    icon(bg="dark", fg='light', fontsize=17, text=' '),    # Icono de calendario

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
