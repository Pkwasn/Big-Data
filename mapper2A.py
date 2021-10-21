#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    city,month,temp = line.split(',')

    print('%s\t%s\t%s\t%s' % (1, city, month, temp))

