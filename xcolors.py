#!/usr/bin/python3

"""imports color codes from ~/.Xresources
   (must be in format "*.color0: #000000")
   and replaces _COLOR0_ up to _COLOR15_ with those."""

import re
import os
import sys
import string

HOME = os.getenv('HOME')
xresources = "{}/.Xresources".format(HOME)

# defaults:
colors = { "_COLOR0_": "#212121",
"_COLOR1_": "#8e2d2d",
"_COLOR2_": "#207f3a",
"_COLOR3_": "#c6cd75",
"_COLOR4_": "#2f3a43",
"_COLOR5_": "#56395b",
"_COLOR6_": "#476e77",
"_COLOR7_": "#a9a9a9",
"_COLOR8_": "#363636",
"_COLOR9_": "#a94c4c",
"_COLOR10_": "#50824c",
"_COLOR11_": "#d5d885",
"_COLOR12_": "#717ace",
"_COLOR13_": "#a05bb7",
"_COLOR14_": "#5493c2",
"_COLOR15_": "#ffffff" }

# first, read ~/.Xresources and get all the color codes:
with open(xresources) as xr:
    for line in xr.readlines():
        result = re.match('\*\.color([0-9]{1,2}):.*(\#[0-9a-fA-F]{6})', line)
        if result:
            #print("{}:{}".format(result.group(1), result.group(2)))
            key = "_COLOR{}_".format(result.group(1))
            colors[key] = result.group(2)

# now replace the placeholders with actual colors (stdin):
if len(sys.argv)<2:
    for line in sys.stdin:
        result = re.match('.*(_COLOR[0-9]{1,2}_).*', line)
        if result:
            line = line.replace(result.group(1), colors[result.group(1)])
        print(line, end="")
# dirty file-hack (sourcefile is argv[1], destination file is argv[2]):
else:
    infile  = sys.argv[1]
    outfile = sys.argv[2]
    if os.path.isfile(infile):
        with open(infile, 'r') as i:
            with open(outfile, 'w') as o:
                for line in i.readlines():
                    result = re.match('.*(_COLOR[0-9]{1,2}_).*', line)
                    if result:
                        try:
                            line = line.replace(result.group(1), colors[result.group(1)])
                        except KeyError:
                            pass
                            # _COLOR16_ give key error, we just leave those

                    o.write(line)
