#!/bin/bash

perc=`pamixer --get-volume`
muted=`pamixer --get-mute`

echo -n "<fc=#C678DD>"

if [ $muted == "true" ]; then
  echo -n "󰝟 "
else
  if [ $perc -le 32 ]; then echo -n " "
  elif [ $perc -le 64 ]; then echo -n " "
  else echo -n " "
  fi
  echo -n "$perc%"
fi

echo -n "</fc>"
