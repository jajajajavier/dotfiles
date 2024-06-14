#!/bin/bash

perc=`pamixer --get-volume`
muted=`pamixer --get-mute`

echo -n "<fc=#C678DD>"

if [ $muted == "true" ]; then
  echo -n "󰝟 Muted"
else
  if [ $perc -le 32 ]; then echo -n " "
  elif [ $perc -le 64 ]; then echo -n " "
  else echo -n " "
  fi

  if [ $perc -le 9 ]; then echo -n "  "
  elif [ $perc -le 99 ]; then echo -n " "
  fi

  echo -n " $perc%"
fi

echo -n "</fc>"
