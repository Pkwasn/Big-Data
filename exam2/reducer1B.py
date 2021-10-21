#!/usr/bin/env python3

import sys

count = {}
last_key = None

for line in sys.stdin:
    line = line.strip()
    key, occur = line.split('\t')
    occur = int(occur)

    if last_key == key:
        count[key] = count[key] + occur
    else:
        count[key] = 1
        last_key = key

for key in count.keys():
    print('Key:%s\tOccurances:%s' % (key, count[key]))
