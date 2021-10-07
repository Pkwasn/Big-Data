#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

regions = {}

for i in range(6):
    regions[i + 1] = ('temp',0)

for line in lines:
    line = line.strip()
    country,landmass,population = line.split(',')
    population = int(population)
    landmass = int(landmass)

    vals = regions[landmass]
    d_country, d_population = vals[0], vals[1]

    if population > d_population:
        regions[landmass] = (country, population)

for key in regions.keys():
    vals = regions[key]
    country, population = vals[0], vals[1]
    print(key, country, population)
