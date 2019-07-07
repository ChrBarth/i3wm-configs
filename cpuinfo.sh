#!/bin/bash

CPUDIR="/sys/bus/cpu/devices/"
for cpu in `ls $CPUDIR`
do
    freqpath="${CPUDIR}${cpu}/cpufreq/"
    echo -n $cpu
    echo -n ": "
    cat "${freqpath}scaling_cur_freq" | awk '/.*/ {printf("%.2f GHz", $1/1000000)}'
    echo -n " ( "
    echo `cat "${freqpath}scaling_governor"` ")"
done

echo

sensors -u | awk '/Package id/ || /Core/ { printf("%s ",$0); getline; printf("%d\n",$2) }'
