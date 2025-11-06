#!/usr/bin/bash

title=`playerctl metadata xesam:title`
artist=`playerctl metadata xesam:artist`
album=`playerctl metadata xesam:album`


out=""
if [[ $(playerctl shuffle) == "On" ]]; then
   out+="  󰒟 "
fi

out+=" $title | $artist"

if [[ $album != "" ]]; then
  out+=", $album"
fi

echo -n {\"text\": \"$out\", \"alt\": \"$(playerctl status)\"}
