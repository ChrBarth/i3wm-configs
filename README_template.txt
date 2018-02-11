conkyrc_template

The template file needs to be processed before it can be used.
To match my .Xresources I use a script that gets the colorcodes
from it and then replaces _COLOR0_, _COLOR1_, etc. with the actual
hex-codes from my .Xresources (*.color0 gets _COLOR0_ and so on).
The script is called xcolors and it has to be run that way:

cat conkyrc_template | xcolors.py \\ > conkyrc

the \\ is used to escape the "#" in the hex-code ("#ffffff" gets "\#ffffff", ...)
