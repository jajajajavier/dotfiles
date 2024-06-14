#!/bin/sh
export PATH=$PATH:$HOME/.local/bin:$HOME/.cabal/bin

/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &
exec /home/javier/.cabal/bin/xmonad
