#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

regions = {}

for i in range(6):
    regions[i + 1] = [0]*10

for line in lines:
    line = line.strip()
    landmass,language = line.split(',')
    language = int(language)
    landmass = int(landmass)

    array = regions[landmass]
    array[language - 1] += 1

for key in regions.keys():
    max_language = max(regions[key])
    print('Landmass: %s, Language: %s, Occurances %s' % (key, int(regions[key].index(max_language)) + 1,max_language ))


