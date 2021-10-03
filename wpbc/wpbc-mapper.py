#!/usr/bin/env python3

'''
Author: Patrick Kwasniak
Date: 10/2/2021
Purpose: Mapper for Wisconsin Prognostic Breast Cancer (WPBC)
    Mapping size of malignant tumor cells
'''

import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')

    tumor_radius = values[3]

    print('%s\t%s' % ('1',tumor_radius))
