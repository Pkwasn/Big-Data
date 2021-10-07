#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    line = line.strip()
    vals = line.split(',')

    landmass = vals[1]
    language = vals[5]

    print('%s,%s' % (landmass, language))
