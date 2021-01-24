#!/bin/bash
# print the amixer volume in percent (for conky/i3)
# print only left value for execbar in conky:

#LEFT=$(amixer -D pulse | grep "Front Left: Playback" | cut -d " " -f 7 | sed -e "s/[^0-9]//g")
##RIGHT=$(amixer -D pulse | grep "Front Right: Playback" | cut -d " " -f 7 | sed -e "s/[^0-9]//g")
#MUTED=$(amixer -D pulse | grep "Front Left: Playback" | cut -d " " -f 8 | sed -e "s/[^onf]//g")
#if [ "$MUTED" == "off" ]
#then
#    LEFT=0
#fi
#echo "${LEFT}"

# all of the above in one simple awk-script:
amixer -D pulse | awk '/Front Left: Playback/ {vol=$5; gsub("[\\[\\]\%]", "", vol); if ($6=="[on]") print vol; else print "0"}' 2>/dev/null
