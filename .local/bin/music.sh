#!/bin/bash

aux=`playerctl metadata`
if [ $? -eq 1 ]; then
	exit 0
fi

title=`playerctl metadata xesam:title`
artist=`playerctl metadata xesam:artist`
album=`playerctl metadata xesam:album`
out=" $title | $artist"

if [[ $album != "" ]]; then
  out+=", $album"
fi

if [ `playerctl shuffle` == "On" ]; then
	echo -n " "
else
	echo -n "  "
fi

if [  `playerctl status` == "Playing" ]; then
	echo -n "  "
else
	echo -n "  "
fi

head -z -c 100 <<< $out

if [ ${#out} > 100 ]; then
	echo -n "..."
fi
