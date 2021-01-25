#!/bin/bash
# a simple starter script for i3blocks
# if we put these commands directly in the i3-config
# i3blocks will crash after an application goes fullscreen
i3blocks &
pid=$!
echo $pid > /tmp/i3blocks.pid
wait $pid
