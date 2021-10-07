#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    vals = line.split(',')

    for letter in vals:
        print('%s\t%s' % (letter, 1))
