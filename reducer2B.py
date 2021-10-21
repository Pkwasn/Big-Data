#!/usr/bin/env python3

import sys

Ptemp = {}
count = {}
last_key = None

for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t')
    val = int(val)

    if last_key == key:
        count[key] = count[key] + 1
        Ptemp[key] = Ptemp[key] + val
    else:
        Ptemp[key] = val
        count[key] = 1
        last_key = key

for key in Ptemp.keys():
    print('Place:%s\tTemp:%s' % (key, Ptemp[key]/count[key]))
