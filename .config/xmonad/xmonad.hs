-- XMonad configuration
import XMonad
import XMonad.Util.EZConfig
import qualified XMonad.StackSet as W
import System.Exit

-- Imports for Xmobar configuration
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.StatusBar.PP
import XMonad.Hooks.StatusBar
import XMonad.Util.SpawnOnce
import XMonad.Util.Run

-- Layout Definitions
import XMonad.Layout.Renamed
import XMonad.Layout.Spacing
import XMonad.Layout.WindowNavigation

import XMonad.Layout.ThreeColumns
import XMonad.Layout.Spiral
import XMonad.Layout.Grid
import XMonad.Layout.TwoPane
import XMonad.Layout.NoBorders

-- Misc
import XMonad.Actions.UpdatePointer
import XMonad.Actions.TiledWindowDragging

-- Some app declaration
myTerminal    = "kitty"   :: String
myWebBrowser  = "firefox" :: String
myFileManager = "pcmanfm" :: String

myBorderWidth = 2
gapSize = 7

-- Workspaces icons
myWorkspaces :: [String]
myWorkspaces = [" \61728 ", " \983609 ", " \985630 ", " \983577 ", " \61912 ", " \62676 ", " \61441 ", " \62599 ", " \62003 "]
-- ["  ", " 󰈹 ", " 󰨞 ", " 󰈙 ", "  ", "  ", "  ", "  ", "  "]

-- Define active layouts
myLayout =  
  -- smartSpacing sets a gap between windows and screen
  renamed [CutWordsLeft 1] . smartBorders . smartSpacing gapSize . windowNavigation $   
  Tall 1 (3/100) (1/2) |||              -- Vertical master and stack layout
  Full |||                              -- Fullscreen layout
  Mirror (Tall 1 (3/100) (13/25)) |||   -- Horisontal master and stack layout 
  ThreeColMid 1 (3/100) (1/2) |||       -- Three Columns, master in mid
  Grid |||                              -- Put all windows in a square grid
  spiral (6/7) |||                      -- Spiral layout, similar to the Fibonacci spiral 
  TwoPane (3/100) (1/2)                 -- Split screen in two windows, master on the left
                                        -- and current focused of a group in the right

-- Execute commands at startup
myStartupHook :: X()
myStartupHook = do
  spawnOnce "~/.config/xmonad/autostart"

-- Key bindings
myKeys :: [(String, X ())]
myModMask = mod4Mask :: KeyMask -- Set windows key as mod key 
myKeys = [
  -- Launch Applications
  ("M-<Return>",    spawn myTerminal),
  ("M-f",           spawn myWebBrowser),
  ("M-e",           spawn myFileManager),
  ("M-a",           spawn "rofi-launcher"),               -- Run applications
  ("M-a",           spawn "rofi-power"),                  -- Launch powermenu
  ("M-a",           spawn "rofi-screenshot"),             -- Take screenshot
  ("M1-C-l",        spawn "betterlockscreen -l dimblur"), -- Lock the screen (M1 = alt) 

  -- Window Management
  ("M-q",   kill),                                -- close window
  ("M-t",       withFocused $ windows . W.sink),  -- toggle floating

  -- Layout management
  ("M-<Space>",   sendMessage NextLayout),        -- Switch between layouts
  ("M-S-<Space>", sendMessage FirstLayout),       -- Restart to default layout

  -- Window movement
  ("M-m",       windows W.focusMaster),           -- Focus to master pane
  ("M-<Tab>",   windows W.focusDown),             -- Focus next window
  ("M-S-<Tab>", windows W.focusUp),               -- Focus prev window
  ("M-h", sendMessage $ Go L),                    -- Focus left window
  ("M-j", sendMessage $ Go D),                    -- Focus down window
  ("M-k", sendMessage $ Go U),                    -- Focus up window
  ("M-l", sendMessage $ Go R),                    -- Focus right window

  -- Swap windows position
  ("M-S-m",     windows W.swapMaster),            -- Swap focused window with the master
  ("M-S-h", sendMessage $ Swap L),                -- Swap left window
  ("M-S-j", sendMessage $ Swap D),                -- Swap down window
  ("M-S-k", sendMessage $ Swap U),                -- Swap up window
  ("M-S-l", sendMessage $ Swap R),                -- Swap right window

  -- Resize
  ("M-C-h", sendMessage Shrink), 
  ("M-C-l", sendMessage Expand),
  ("M-C-n", refresh), -- Restore normal size

  -- Audio
  ("<XF86AudioRaiseVolume>", spawn "pamixer -i 5"),
  ("<XF86AudioLowerVolume>", spawn "pamixer -d 5"),
  ("<XF86AudioMute>", spawn "pamixer -t"),                -- Toggle mute the speakers
  ("<XF86AudioMicMute>",   spawn "pamixer --source <input_source> -t"),  -- Toggle mute the mic

  -- Brightness
  ("<XF86MonBrightnessUp>",   spawn "brightnessctl s +5%"),
  ("<XF86MonBrightnessDown>", spawn "brightnessctl s 5%-"),
  
  -- Keyboard led
  -- ("<XF86KbdBrightnessUp>",   spawn "brightnessctl -d asus::kbd_backlight s +1"),
  -- ("<XF86KbdBrightnessDown>", spawn "brightnessctl -d asus::kbd_backlight s 1-"),

  -- Quit and restart Xmonad
  ("M-C-q", io exitSuccess),
  ("M-C-r", spawn "xmonad --recompile && xmonad --restart")
  ]
  ++ -- Change the current workspace
  [("M-" ++ show n, windows $ W.greedyView x ) | (n, x) <- zip [1..9] myWorkspaces ]
  ++ -- Move focused windows to worspace
  [("M-S-" ++ show n, windows $ W.shift x) | (n, x) <- zip [1..9] myWorkspaces]

-- Mouse bindings
myMouseBindings :: [( (ButtonMask, Button), Window -> X() )]
myMouseBindings = [
  ( (myModMask .|. shiftMask , button1), dragWindow)  -- Drag window to change position
  ]


main :: IO()
main = do
  startXmobar <- spawnPipe "xmobar ~/.config/xmobar/xmobar.hs"

  xmonad . xmobarProp $ def {
  modMask  = myModMask,
  terminal = myTerminal,
  workspaces = myWorkspaces,
  keys = (`mkKeymap` myKeys), 

  borderWidth = myBorderWidth,
  normalBorderColor = background,
  focusedBorderColor = blue,

  layoutHook = myLayout,
  startupHook = myStartupHook,
  logHook = dynamicLogWithPP xmobarPP {
    ppSep = "<fc="++gray++"> \61524 </fc>", 
    ppHiddenNoWindows = xmobarColor gray "",
    ppHidden = xmobarColor foreground "",
    ppCurrent = xmobarColor blue "" . wrap "[" "]",
    ppUrgent = xmobarColor yellow "" . wrap "!" "!",
    ppLayout = xmobarColor cyan "" . wrap "[" "]",
    ppTitle = xmobarColor foreground "" . shorten 60,
    ppOrder = \(ws:l:e) -> [ws, l], -- comment if you want the window title
    ppOutput = hPutStrLn startXmobar
  } 
  >> updatePointer (0.5 , 0.5) (0.5 , 0.5) -- set pointer position
} `additionalMouseBindings` myMouseBindings

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
