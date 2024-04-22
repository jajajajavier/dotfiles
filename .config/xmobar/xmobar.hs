Config {
  font = "xft:JetBrainsMono NF",
  position       = TopSize C 100 26,
  bgColor = "#1e2127",
  fgColor = "#abb2bf",
  lowerOnStart = True,
  hideOnStart = False,
  allDesktops = True,
  persistent = True,
  commands = [ 
    Run Com "echo" ["<fc=#4C566A>\xf053</fc>"]  "sep" 1,
    Run Com "/home/javier/.config/xmobar/script/battery.sh" [] "batt" 200,
    Run Com "/home/javier/.config/xmobar/script/audio.sh" [] "volume" 5,
    Run Com "/home/javier/.config/xmobar/script/brightness.sh" [] "brightness" 5,
    Run Date "<fc=#61AFEF>\62635 %H:%M</fc>" "time" 10,
    Run Date "<fc=#56B6C2>󱨰 %a, %d %b</fc>" "date" 100000,
    Run UnsafeStdinReader
  ],
  sepChar = "%",
  alignSep = "}{",
  template = " %UnsafeStdinReader% }{ %sep% %volume% %sep% %brightness% %sep% %batt% %sep% %date% %sep% %time% "
}
