#!/bin/sh
export PATH=$PATH:~/.cabal/bin

/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &
exec /home/javier/.cabal/bin/xmonad
