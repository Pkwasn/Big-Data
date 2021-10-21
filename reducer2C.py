#!/usr/bin/env python3

import sys

Mtemp = {}
count = {}
last_key = None

for line in sys.stdin:
    line = line.strip()
    key, temp = line.split('\t')
    temp = int(temp)

    if last_key == key:
        Mtemp[key] = Mtemp[key] + temp
        count[key] = count[key] + 1
    else:
        Mtemp[key] = temp
        count[key] = 1
        last_key = key

for key in Mtemp.keys():
    print('Month:%s\tAverage Temp:%s' % (key, Mtemp[key]/count[key]))
