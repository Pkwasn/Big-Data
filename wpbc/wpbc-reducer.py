#!/usr/bin/env python3

'''
Author: Patrick Kwasniak
Date: 10/2/2021
Purpose: Reducer for Wisconsin Prognostic Breast Cancer (WPBC)

	1. What is the average radius of malignant tumor cells
	2. How many cases are there where the benign tumor cells have more radius
	than the average clump thickness/tumor radius of malignant tumor cells
'''

import sys

lines = sys.stdin.readlines()
average_tumor = {}
count = {}
last_key = None

for line in lines:
	line = line.strip()
	key, radius = line.split('\t')
	radius = float(radius)

	if last_key == key:
            average_tumor[key] = average_tumor[key] + radius
            count[key] += 1
	else:
            average_tumor[key] = radius
            count[key] = 1
            last_key = key

for key in average_tumor.keys():
    print('%s: %.2f %s' % (key + " Average Tumor Size",average_tumor[key]/count[key],'cm'))

large_benign_count = {'B':0}

for line in lines:
    line = line.strip()
    key, radius = line.split('\t')
    radius = float(radius)

    if key == "B" and radius > average_tumor['M']/count['M']:
        large_benign_count['B'] += 1


print('%s %s cases' % ('Number of Cases w/ Benign > Avg Malignant:',large_benign_count['B']))
