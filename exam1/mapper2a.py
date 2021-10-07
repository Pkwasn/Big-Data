#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    line = line.strip()
    vals = line.split(',')

    country = vals[0]
    landmass = vals[1]
    population = vals[4]

    print('%s,%s,%s' % (country, landmass, population))
