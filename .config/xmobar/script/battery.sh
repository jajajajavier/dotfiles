#!/bin/bash

perc=`upower -i $(upower -e | grep BAT) | grep "percentage:" | sed 's/[^0-9]*//g'`
state=`upower -i $(upower -e | grep BAT) | grep "state:" | sed 's/ *state: *//g'`


if [ $state == "charging" -o $state == "fully-charged" ]; then
    echo -n "<fc=#98C379>"
else
  if [ $perc -le 5 ]; then echo -n "<fc=#E06C75> "
  elif [ $perc -le 25 ]; then echo -n "<fc=#E5C07B> "
  elif [ $perc -le 50 ]; then echo -n "<fc=#98C379> "
  elif [ $perc -le 75 ]; then echo -n "<fc=#98C379> "
  else echo -n "<fc=#98C379> "
  fi
fi

if [ $perc -le 9 ]; then echo -n "  "
elif [ $perc -le 99 ]; then echo -n " "
fi

echo -n " $perc%</fc>"