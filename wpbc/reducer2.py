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
last_key = None

for line in lines:
	line = line.strip()
	key, radius = line.split('\t')
	radius = float(radius)
	
	if last_key == key:
		average_tumor[key] = (average_tumor[key] + radius)/2
	elif last_key == None:
		average_tumor[key] = radius
		last_key = key

print('\n%s\t%.2f %s' % ('Average Tumor Size:', average_tumor[last_key],'units'))

tumor_count = 0 									# Count for how many cases
											# have more radius than the 
for line in lines:									# average clump thickness
	line = line.strip()
	key, radius = line.split('\t')
	radius = float(radius)	
	
	if radius > average_tumor[last_key]:
		tumor_count += 1

print('%s\t%s %s' % ('Number of tumors with radius larger than average:',tumor_count,'Cases\n'))
