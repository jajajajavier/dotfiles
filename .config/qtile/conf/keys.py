# Keys Config
#
# por javier
# https://github.com/jajajajavier


from libqtile.config import Key, Drag
from libqtile.lazy import lazy


mod = "mod4"                    # Tecla windows
Alt = "mod1"                    # Tecla Alt izquierda 


#-------------------- combinaciones de teclado-------------------- 

# En desc= estan las teclas y combinaciones
# Arriba de cada configuracion una breve explicacion

keys = [
    
    # >>>>>>>>>>>>>>>|Ventanas|<<<<<<<<<<<<<<<


    # cambia distribucion de ventanas. 
    # Para agregar o quitar distribuciones editar: ~/.config/qtile/conf/layout.py
    Key([mod, "shift"], "Tab", lazy.next_layout(),              desc="Win + Shift + Tab"),
    
    # Mueve la ventana a otra posicion, sea arriba, abajo, izquierda o derecha
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),     desc="Win + Shift + Flecha izquierda"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),   desc="Win + Shift + Flecha derecha"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),     desc="Win + Shift + Flecha abajo"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),         desc="Win + Shift + Flecha arriba"),

    # Redimensiona la ventana, columna o fila hacia cualquier direccion 
    Key([mod, "control"], "Left", lazy.layout.grow_left(),      desc="Win + Control izq. + Flecha izquierda"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),    desc="Win + Control izq. + Flecha derecha"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),      desc="Win + Control izq. + Flecha abajo"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(),          desc="Win + Control izq. + Flecha arriba"),
    
    # Cambiar la ventana enfocada a arriba, izquierda, derecha o abajo de esta 
    Key([mod], "Left", lazy.layout.left(),                      desc="Win + Flecha izquierda"),
    Key([mod], "Right", lazy.layout.right(),                    desc="Win + Flecha derecha"),
    Key([mod], "Down", lazy.layout.down(),                      desc="Win + Flecha abajo"),
    Key([mod], "Up", lazy.layout.up(),                          desc="Win + Flecha arriba"),

    # Tabear a la ventana siguiente
    Key([Alt], "Tab", lazy.layout.next(),                       desc="Alt + Tab"),

    # Redimensiona las ventanas a su estado normal 
    Key([mod], "Delete", lazy.layout.normalize(),               desc="Win + Suprimir"),

    # Cierra la ventana enfocada
    Key([mod], "q", lazy.window.kill(),                         desc="Win + q"),

    # Traer una ventana al frente. La saca del mosaico 
    Key([mod], "Prior", lazy.window.bring_to_front(),           desc="Win + Re pag "),
    
    # Ventana completa
    Key([mod], "F11", lazy.window.toggle_fullscreen(),          desc="Win + F11"),

    # Poner ventana flotante en el mosaico 
    Key([mod], "Next", lazy.window.toggle_floating(),           desc="Win + Av pag"),

    
    # >>>>>>>>>>>>>>>|Qtile|<<<<<<<<<<<<<<<
    

    # Reiniciar Qtile
    Key([mod, "control"], "r", lazy.restart(),                  desc="Win + Control izq. + r"),

    # Apagar Qtile
    Key([mod, "control"], "q", lazy.shutdown(),                 desc="Win + Control izq. + q"),
    
     
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
   
   
    # Terminal Alacritty 
    Key([mod], "t", lazy.spawn("alacritty"),                                desc="Win + T"),
    
    # Menu de ventanas
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show"),                 desc="Win + Shift + Enter"),
    
    # arrancar programas
    Key([mod], "Return", lazy.spawn("rofi -show run"),                      desc="Win + Enter"),
    
    # Firefox
    Key([mod], "b", lazy.spawn("firefox"),                                  desc="Win + b"),
    
    # Gestor de archivos ( Ranger )
    Key([mod], "BackSpace", lazy.spawn("alacritty --command ranger"),       desc="Win + Borrar"),
    
    # screnshot pantalla completa guardado en el /home/screenshots,
    # tienes que crear la carpeta con 
    # $ mkdir screenshots
    Key([], "Print", lazy.spawn("scrot -e 'mv $f ~/screenshots/'"),                 desc="Imprent pant"),

    # screneshot pantalla commpleta en el clipboard
    Key([mod], "s", lazy.spawn("scrot '/tmp/%F_%T_$wx$h.png' -e"+ 
        " 'xclip -selection clipboard -target image/png -i $f && rm $f'"),          desc="Win + s"),

    # screenshoot de seleccion de region en el clipboard
    Key([mod, "shift"], "s", lazy.spawn("scrot '/tmp/%F_%T_$wx$h.png'"+ 
        " -s -e 'xclip -selection clipboard -target image/png -i $f && rm $f'"),    desc="Win + Shift + s"), 
]


# >>>>>>>>>>>>>>>|Mouse|<<<<<<<<<<<<<<<

# Sacar y redimensionar ventana
mouse = [
    
    # Flota la ventana
    Drag([mod, "shift"], "Button1", lazy.window.set_position_floating(),    desc="Win + Shift + Click izq.",
        start=lazy.window.get_position()),
    
    # Redimensionar la ventana flotante
    Drag([mod, "shift"], "Button3", lazy.window.set_size_floating(),        desc="Win + Shift + Click der.",
        start=lazy.window.get_size()),
]
