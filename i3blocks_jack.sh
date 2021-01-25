#!/bin/bash
# is jack up and running?
JACK_STATUS=$(jack_control status | tail -n 1)
echo "JACK: $JACK_STATUS"
echo "$JACK_STATUS"
if [ "$JACK_STATUS" = "stopped" ]; then
    echo "#FF0000"
else
    echo "#00FF00"
fi
