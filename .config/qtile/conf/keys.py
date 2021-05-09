# Keys Config
#
# por javier
# https://github.com/jajajajavier


from libqtile.config import Key, Drag
from libqtile.lazy import lazy


Win = "mod4"                    # Tecla windows
Alt = "mod1"                    # Tecla Alt izquierda 
MyTerm = "alacritty"            # Cambialo dependiendo de tu emulador de terminal
MyBrowser = "firefox"           # Camialo dependiendo de tu navegador peferido
MyFileManager = "Thunar"        # Cambialo segun tu administrador de archivos

#-------------------- combinaciones de teclado-------------------- 

# En desc= estan las teclas y combinaciones
# Arriba de cada configuracion una breve explicacion

keys = [
    
    # >>>>>>>>>>>>>>>|Ventanas|<<<<<<<<<<<<<<<

    # cambia distribucion de ventanas. 
    # Para agregar o quitar distribuciones editar: ~/.config/qtile/conf/layout.py
    Key([Win, "shift"], "Tab", lazy.next_layout(),           desc="Win + Shift + Tab"),
    
    # Mueve la ventana a otra posicion, sea ↑ ↓ ← →
    Key([Win, "shift"], "h", lazy.layout.shuffle_left(),     desc="Win + Shift + H"),
    Key([Win, "shift"], "l", lazy.layout.shuffle_right(),    desc="Win + Shift + L"),
    Key([Win, "shift"], "j", lazy.layout.shuffle_down(),     desc="Win + Shift + J"),
    Key([Win, "shift"], "k", lazy.layout.shuffle_up(),       desc="Win + Shift + K"),

    # Redimensiona la ventana, columna o fila
    Key([Win, "control"], "h", lazy.layout.grow_left(),      desc="Win + Control izq. + H"),
    Key([Win, "control"], "l", lazy.layout.grow_right(),     desc="Win + Control izq. + L"),
    Key([Win, "control"], "j", lazy.layout.grow_down(),      desc="Win + Control izq. + J"),
    Key([Win, "control"], "k", lazy.layout.grow_up(),        desc="Win + Control izq. + K"),
    
    # Cambiar la ventana enfocada ↑ ↓ ← →
    Key([Win], "h", lazy.layout.left(),                      desc="Win + H"),
    Key([Win], "l", lazy.layout.right(),                     desc="Win + L"),
    Key([Win], "j", lazy.layout.down(),                      desc="Win + J"),
    Key([Win], "k", lazy.layout.up(),                        desc="Win + K"),

    # Tabear a la ventana siguiente
    Key([Alt], "Tab", lazy.layout.next(),                       desc="Alt + Tab"),

    # Redimensiona las ventanas a su estado normal 
    Key([Win], "Delete", lazy.layout.normalize(),               desc="Win + Suprimir"),

    # Cierra la ventana enfocada
    Key([Win], "q", lazy.window.kill(),                         desc="Win + q"),

    # Traer una ventana al frente. La saca del mosaico 
    Key([Win, "shift"], "space", lazy.window.bring_to_front(),  desc="Win + Shift + Espacio"),
    
    # Ventana completa
    Key([Win], "F11", lazy.window.toggle_fullscreen(),          desc="Win + F11"),

    # Poner ventana flotante en el mosaico 
    Key([Win], "space", lazy.window.toggle_floating(),          desc="Win + Espacio"),

    
    # >>>>>>>>>>>>>>>|Qtile|<<<<<<<<<<<<<<<
    

    # Reiniciar Qtile
    Key([Win, "control"], "r", lazy.restart(),                  desc="Win + Control izq. + r"),

    # Apagar Qtile
    Key([Win, "control"], "q", lazy.shutdown(),                 desc="Win + Control izq. + q"),
    
     
    # >>>>>>>>>>>>>>>|Audio y brillo|<<<<<<<<<<<<<<<

   
    # Audio, pamixer

    # Bajar volumen  
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 2"),     desc="Fn + Flecha abajo"),

    # Subir volumen 
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 2"),     desc="Fn + Flecha arriba"),


    # Brillo, xbacklight 

    # Subir brillo un 5%
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -inc 5%"),   desc="Fn + Flecha izquierda"),

    # Bajar brillo un 5%
    Key([], "XF86MonBrightnessUp", lazy.spwan("xbacklight -dec 5%"),     desc="Fn + Flecha derecha"),


   # >>>>>>>>>>>>>>>|Otros|<<<<<<<<<<<<<<<
   
   
    # Terminal 
    Key([Win], "Return", lazy.spawn(MyTerm),                                 desc="Win + Enter"),
    
    # Menu de ventanas
    Key([Win, "shift"], "BackSpace", lazy.spawn("rofi -show"),              desc="Win + Shift + Borrar"),
    
    # arrancar programas
    Key([Win], "BackSpace", lazy.spawn("rofi -show run"),                   desc="Win + Borrar"),
    
    # Navegador
    Key([Win], "b", lazy.spawn(MyBrowser),                                  desc="Win + b"),
    
    # Administrador de archivos
    Key([Win], "f", lazy.spawn(MyFileManager),                              desc="Win + F"),

    # screnshot pantalla completa guardado en el /home/screenshots,
    # tienes que crear la carpeta con 
    # $ mkdir screenshots
    Key([], "Print", lazy.spawn("scrot -e 'mv $f ~/screenshots/'"),                 desc="Imprent pant"),

    # screneshot pantalla commpleta en el clipboard
    Key([Win], "s", lazy.spawn("scrot '/tmp/%F_%T_$wx$h.png' -e"+ 
        " 'xclip -selection clipboard -target image/png -i $f && rm $f'"),          desc="Win + s"),

    # screenshoot de seleccion de region en el clipboard
    Key([Win, "shift"], "s", lazy.spawn("scrot '/tmp/%F_%T_$wx$h.png'"+ 
        " -s -e 'xclip -selection clipboard -target image/png -i $f && rm $f'"),    desc="Win + Shift + s"), 
]


# >>>>>>>>>>>>>>>|Mouse|<<<<<<<<<<<<<<<

# Sacar y redimensionar ventana
mouse = [
    
    # Flota la ventana
    Drag([Win, "shift"], "Button1", lazy.window.set_position_floating(),    desc="Win + Shift + Click izq.",
        start=lazy.window.get_position()),
    
    # Redimensionar la ventana flotante
    Drag([Win, "shift"], "Button3", lazy.window.set_size_floating(),        desc="Win + Shift + Click der.",
        start=lazy.window.get_size()),
]
