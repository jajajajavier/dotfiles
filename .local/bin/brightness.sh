#!/bin/bash

perc=`brightnessctl i | grep -o -E "[0-9]+%" | sed 's/ *% *//g'`

echo -n "<fc=#ABB2BF>"

if [ $perc -le 25 ]; then echo -n "󰃞 "
elif [ $perc -le 50 ]; then echo -n "󰃝 "
elif [ $perc -le 75 ]; then echo -n "󰃟 "
else echo -n "󰃠 "
fi

if [ $perc -le 9 ]; then echo -n "  "
elif [ $perc -le 99 ]; then echo -n " "
fi

echo -n "$perc%</fc>"
