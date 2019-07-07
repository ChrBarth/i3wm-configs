#!/usr/bin/env python3

import subprocess
#import re

# get the cpu-temerature(s) from lm-sensors

# sensors -u outputs the temperature-data in raw
CMD = ['sensors', '-u']

# get output from CMD:
output = subprocess.run(CMD, stdout=subprocess.PIPE)
result = list(output.stdout.decode('utf-8').split("\n"))

temp1 = 0
temp2 = 0
temp3 = 0

for l in enumerate(result):
    #print("{} --> {}".format(l[0], l[1]))
    if 'Package id 0' in l[1]:
        temp1 = float(result[l[0]+1].split(": ")[1])
        #print("Temp1: {}".format(int(temp1)))
    if 'Core 0' in l[1]:
        temp2 = float(result[l[0]+1].split(": ")[1])
        #print("Temp2: {}".format(int(temp2)))
    if 'Core 1' in l[1]:
        temp3 = float(result[l[0]+1].split(": ")[1])
        #print("Temp3: {}".format(int(temp3)))

print("{}°C / {}°C / {}°C".format(int(temp1), int(temp2), int(temp3)))
