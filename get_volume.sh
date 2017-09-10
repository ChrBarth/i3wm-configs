#!/bin/bash
# print the amixer volume in percent (for conky/i3)
# print only left value for execbar in conky:

LEFT=$(amixer -D pulse | grep "Front Left: Playback" | cut -d " " -f 7 | sed -e "s/[^0-9]//g")
#RIGHT=$(amixer -D pulse | grep "Front Right: Playback" | cut -d " " -f 7 | sed -e "s/[^0-9]//g")
echo "${LEFT}"
