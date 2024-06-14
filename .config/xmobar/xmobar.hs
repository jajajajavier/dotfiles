import Xmobar

config :: Config
config = defaultConfig {
  font = "xft:JetBrainsMono NF",
  position = TopSize C 100 26,
  bgColor = "#1e2127",
  fgColor = "#abb2bf",
  lowerOnStart = True,
  hideOnStart = False,
  allDesktops = True,
  persistent = True,
  commands = [ 
    Run $ Com "echo" ["<fc=#4C566A>\61523</fc>"]  "sep" 1000000000,
    Run $ Com "battery.sh" [] "batt" 200,
    Run $ Com "audio.sh" [] "volume" 5,
    Run $ Com "brightness.sh" [] "brightness" 5,
    Run $ Date "<fc=#61AFEF>\62635 %H:%M</fc>" "time" 10,
    Run $ Date "<fc=#56B6C2>\989744 %a, %d %b</fc>" "date" 100000,
    Run UnsafeStdinReader
  ],
  sepChar = "%",
  alignSep = "}{",
  template = " %UnsafeStdinReader% }{ %sep% %volume% %sep% %brightness% %sep% %batt% %sep% %date% %sep% %time% "
}

main :: IO()
main = xmobar config
