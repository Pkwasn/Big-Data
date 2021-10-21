#!/usr/bin/env python3

import sys

min_temp = {}
last_key = None

for line in sys.stdin:
    line = line.strip()
    key, city, month, temp = line.split('\t')

    if last_key == key:
        vals = min_temp[key]
        Mtemp = vals[2]
        if temp < Mtemp:
            min_temp[key] = (city, month, temp)
        else:
            continue
    else:
        last_key = key
        min_temp[key] = (city, month, temp)

for key in min_temp.keys():
    print(min_temp[key])
