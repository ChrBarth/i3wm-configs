#!/bin/bash
# is jack up and running?
JACK_STATUS=$(jack_control status | tail -n 1)
#echo "$JACK_STATUS"
if [ "$JACK_STATUS" = "stopped" ]; then
    echo "❌"
    echo "#FF0000"
else
    echo "✅"
    echo "#00FF00"
fi
