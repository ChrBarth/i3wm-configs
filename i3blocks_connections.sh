#!/bin/bash
#checks if system_captureX is connected to system_playbackX

#jack_lsp -c | awk 'BEGIN { FS="\n"; con=0 } /^[a-zA-Z]/ { line=$1 } /   system:capture_[12]/ { if(match(line, "system:playback")) {print line, $1; con=con+1}} END { print "Connections:", con }'
CON=$(jack_lsp -c | awk 'BEGIN { FS="\n"; con=0 } /^[a-zA-Z]/ { line=$1 } /   system:capture_[12]/ { if(match(line, "system:playback")) {con=con+1}} END { print con }')
if [[ $CON -eq 2 ]]; then
    #echo "(connected)"
    echo 😸
    echo "#00FF00"
else
    #echo "(not connected)"
    echo 🙀
    echo "#AAAAAA"
fi
