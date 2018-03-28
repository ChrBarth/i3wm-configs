#!/bin/bash

# removes all '`"-characters from song titles and artists
# to prevent "Error: Could not parse JSON..." in i3bar
# (conky does not have an option to escape or filter these
# characters...
mpc status -f "%artist%\t%title%" | sed -e 's/[\"]//g' -e "s/[\'\`\']//g" -n -e 's/\t/ - /g p'
