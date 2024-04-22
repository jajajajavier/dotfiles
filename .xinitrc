#!/bin/sh

setxkbmap latam
~/.fehbg &
picom &

stalonetray &
nm-applet &

exec /home/javier/.cabal/bin/xmonad
