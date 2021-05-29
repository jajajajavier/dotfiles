# Keys Config
#
# by javier
# https://github.com/jajajajavier


from libqtile.config import Key, Drag
from libqtile.lazy   import lazy
from libqtile        import qtile 

Win = "mod4"                                # Windows key
Alt = "mod1"                                # Alt key 
MyTerm = "alacritty"
MyBrowser = "firefox"
MyFileManager = "Thunar"


#-------------------- Keybindings-------------------- 
keys = [
    
    # >>>>>>>>>>>>>>>|Windows|<<<<<<<<<<<<<<<

    # Change the windows orientation
    # for add or remove windows orientation edit: ~/.config/qtile/conf/layout.py
    Key([Win, "shift"], "Tab", lazy.next_layout(),           desc="Win + Shift + Tab"),
    
    # Move windows to another position
    Key([Win, "shift"], "h", lazy.layout.shuffle_left(),     desc="Win + Shift + H"),
    Key([Win, "shift"], "l", lazy.layout.shuffle_right(),    desc="Win + Shift + L"),
    Key([Win, "shift"], "j", lazy.layout.shuffle_down(),     desc="Win + Shift + J"),
    Key([Win, "shift"], "k", lazy.layout.shuffle_up(),       desc="Win + Shift + K"),

    # Resize the windows
    Key([Win, "control"], "h", lazy.layout.grow_left(),      desc="Win + Control izq. + H"),
    Key([Win, "control"], "l", lazy.layout.grow_right(),     desc="Win + Control izq. + L"),
    Key([Win, "control"], "j", lazy.layout.grow_down(),      desc="Win + Control izq. + J"),
    Key([Win, "control"], "k", lazy.layout.grow_up(),        desc="Win + Control izq. + K"),
    
    # Change the focus windows 
    Key([Win], "h", lazy.layout.left(),                      desc="Win + H"),
    Key([Win], "l", lazy.layout.right(),                     desc="Win + L"),
    Key([Win], "j", lazy.layout.down(),                      desc="Win + J"),
    Key([Win], "k", lazy.layout.up(),                        desc="Win + K"),

    # Tabing
    Key([Alt], "Tab", lazy.layout.next(),                       desc="Alt + Tab"),

    # Resize the windows to normal size  
    Key([Win], "Delete", lazy.layout.normalize(),               desc="Win + Supr),

    # Close the focus windows
    Key([Win], "q", lazy.window.kill(),                         desc="Win + q"),
    
    # Fullscreen 
    Key([Win], "F11", lazy.window.toggle_fullscreen(),          desc="Win + F11"),

    # Place windows on tiling or Bring to front 
    Key([Win], "space", lazy.window.toggle_floating(),          desc="Win + Space"),

    
    # >>>>>>>>>>>>>>>|Qtile|<<<<<<<<<<<<<<<

    # Restart Qtile
    Key([Win, "control"], "r", lazy.restart(),                  desc="Win + Control + r"),

    # Shutdown Qtile
    Key([Win, "control"], "q", lazy.shutdown(),                 desc="Win + Control + q"),
    
     
    # >>>>>>>>>>>>>>>|Audio and brightness|<<<<<<<<<<<<<<<

    # Audio, pamixer ----------
    # Decrease volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 2"),     desc="Fn + Down"),

    # Increase volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 2"),     desc="Fn + Up"),
    

    # Brillo, xbacklight ------
    # Increase brightness  5%
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -inc 5%"),   desc="Fn + Left"),

    # Decrease Brightness  5%
    Key([], "XF86MonBrightnessUp", lazy.spwan("xbacklight -dec 5%"),     desc="Fn + Right"),


   # >>>>>>>>>>>>>>>|Otros|<<<<<<<<<<<<<<<
   
    # Terminal 
    Key([Win], "Return", lazy.spawn(MyTerm),                                desc="Win + Enter"),
    
    # WIndows menu
    Key([Win, "shift"], "BackSpace", lazy.spawn("rofi -show"),              desc="Win + Shift + Backspace"),
    
    # Run apps
    Key([Win], "BackSpace", lazy.spawn("rofi -show run"),                   desc="Win + Backspace"),
    
    # Pavucontrol
    Key([Win], "v", lazy.spawn("pavucontrol"),                              desc="Win + v"),
        
    # Browser
    Key([Win], "b", lazy.spawn(MyBrowser),                                  desc="Win + b"),
    
    # File manager
    Key([Win], "f", lazy.spawn(MyFileManager),                              desc="Win + F"),

    # Fullscreen screenshot saving in the /home/screenshots folder
    # you need create the screenshot folder with
    # $ mkdir screenshots
    Key([], "Print", lazy.spawn("scrot -e 'mv $f ~/screenshots/'"),                 desc="Imprent pant"),

    # Fullscreen screenshot saving in the clipboard
    Key([Win], "s", lazy.spawn("scrot '/tmp/%F_%T_$wx$h.png' -e"+ 
        " 'xclip -selection clipboard -target image/png -i $f && rm $f'"),          desc="Win + s"),

    # Screenshot of selected area saving in the clipboard
    Key([Win, "shift"], "s", lazy.spawn("scrot '/tmp/%F_%T_$wx$h.png'"+ 
        " -s -e 'xclip -selection clipboard -target image/png -i $f && rm $f'"),    desc="Win + Shift + s"), 
]


# >>>>>>>>>>>>>>>|Mouse|<<<<<<<<<<<<<<<
mouse = [
    
    # Float windows
    Drag([Win, "shift"], "Button1", lazy.window.set_position_floating(),    desc="Win + Shift + Left click",
        start=lazy.window.get_position()),
    
    # Resize the floating windows
    Drag([Win, "shift"], "Button3", lazy.window.set_size_floating(),        desc="Win + Shift + Right click",
        start=lazy.window.get_size()),
]
