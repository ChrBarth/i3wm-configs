#!/usr/bin/env python3

import subprocess

# get the cpu-temerature(s) from lm-sensors
# for intel i3 on MSI B75A-G43

# sensors -u outputs the temperature-data in raw
CMD = ['sensors', '-u']

# get output from CMD:
output = subprocess.run(CMD, stdout=subprocess.PIPE)
result = list(output.stdout.decode('utf-8').split("\n"))

temp1 = 0
temp2 = 0
temp3 = 0

for l in enumerate(result):
    if 'Package id 0' in l[1]:
        temp1 = float(result[l[0]+1].split(": ")[1])
    if 'Core 0' in l[1]:
        temp2 = float(result[l[0]+1].split(": ")[1])
    if 'Core 1' in l[1]:
        temp3 = float(result[l[0]+1].split(": ")[1])

print("{}°C / {}°C / {}°C".format(int(temp1), int(temp2), int(temp3)))
