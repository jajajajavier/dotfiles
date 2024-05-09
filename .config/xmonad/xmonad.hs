import XMonad
import XMonad.Util.EZConfig
import qualified XMonad.StackSet as W

-- Xmobar needed
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.StatusBar
import XMonad.Hooks.StatusBar.PP
import XMonad.Util.Run

-- Layouts
import XMonad.Layout.WindowNavigation
import XMonad.Layout.Spacing

-- Misc
import XMonad.Actions.UpdatePointer
import qualified XMonad as C

myTerminal :: String
myTerminal = "alacritty"

myWorkspaces :: [String]
myWorkspaces = [" \61728 ", " \983609 ", " \985630 ", " \983577 ", " \61912 ", " \62676 ", " \61441 ", " \62599 ", " \62003 "]
-- ["  ", " 󰈹 ", " 󰨞 ", " 󰈙 ", "  ", "  ", "  ", " 󰡨 ", "  "]

myLayout = 
  spacing 5 $
  
  windowNavigation (Tall 1 (3/100) (1/2))
  ||| Full

myKeys :: [(String, X ())]
myKeys = [
  ("M-<Return>",  spawn myTerminal),
  ("M-b",         spawn "firefox"),
  ("M-f",         spawn "pcmanfm"),
  ("M-d",         spawn "~/.config/rofi/scripts/launcher_t3"),
  ("M-<Backspace>",         spawn "~/.config/rofi/scripts/powermenu_t2"),
  ("M-s",         spawn "~/.config/rofi/applets/bin/screenshot.sh"),

  ("M-<Tab>",   windows W.focusDown),
  ("M-S-<Tab>", windows W.focusDown),
  ("M-t",       withFocused $ windows . W.sink),
  ("M-m",       windows W.focusMaster),
  ("M-S-m",     windows W.swapMaster),

  ("M-<Space>",   sendMessage NextLayout),
  ("M-S-<Space>", sendMessage FirstLayout),

  ("M-h", sendMessage $ Go L),
  ("M-j", sendMessage $ Go D),
  ("M-k", sendMessage $ Go U),
  ("M-l", sendMessage $ Go R),

  ("M-S-h", sendMessage $ Swap L),
  ("M-S-j", sendMessage $ Swap D),
  ("M-S-k", sendMessage $ Swap U),
  ("M-S-l", sendMessage $ Swap R),


  ("M-C-h", sendMessage Shrink),
  ("M-C-l", sendMessage Expand),
  ("M-C-n", refresh),
  -- Audio
  ("<XF86AudioRaiseVolume>", spawn "pamixer -i 5"),
  ("<XF86AudioLowerVolume>", spawn "pamixer -d 5"),
  ("<XF86AudioMute>", spawn "pamixer -t"),
  -- Brightness
  ("<XF86MonBrightnessUp>", spawn "brightnessctl s +5%"),
  ("<XF86MonBrightnessDown>", spawn "brightnessctl s 5%-"),

  ("M-q",   kill),
  ("M-C-q", spawn "kill -9 -1"),
  ("M-C-r", spawn "xmonad --recompile && xmonad --restart")
  ]
  ++ -- Change the current workspace
  [("M-" ++ show n, windows $ W.greedyView x ) | (n, x) <- zip [1..9] myWorkspaces ]
  ++ -- Move focused windows to worspace
  [("M-S-" ++ show n, windows $ W.shift x) | (n, x) <- zip [1..9] myWorkspaces]

main :: IO()
main = do
  startXmobar <- spawnPipe "xmobar ~/.config/xmobar/xmobar.hs"

  xmonad . xmobarProp $ def {
  modMask  = mod4Mask,
  terminal = myTerminal,
  workspaces = myWorkspaces,
  keys = (`mkKeymap` myKeys),

  borderWidth = 1,
  normalBorderColor = background,
  focusedBorderColor = blue,

  layoutHook = myLayout,
  logHook = dynamicLogWithPP xmobarPP {
    ppOutput = hPutStrLn startXmobar,
    ppTitle = xmobarColor foreground "" . shorten 45,
    ppCurrent = xmobarColor blue "" . wrap "[" "]",
    ppHidden = xmobarColor foreground "",
    ppHiddenNoWindows = xmobarColor gray "",
    ppUrgent = xmobarColor yellow "" . wrap "!" "!",
    ppLayout = xmobarColor cyan "" . wrap "[" "]",
    ppOrder = \(ws:l:e) -> [ws, l],
    ppSep = "<fc=#4C566A> | </fc>"
  } 
  >> updatePointer (0.5 , 0.5) (0.5 , 0.5) -- set pointer position
}

yellow, blue, gray, green, cyan, magenta, red, foreground, background :: String
yellow      = "#E5C07B"
blue        = "#61AFEF" 
green       = "#98C379"
red         = "#E06C75"
cyan        = "#56B6C2"
gray        = "#4C566A"
magenta     = "#C678DD"
foreground  = "#ABB2BF"
background  = "#1E2127"
