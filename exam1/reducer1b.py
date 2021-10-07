#!/usr/bin/env python3

import sys

occurance = {}
last_key = None

for line in sys.stdin:
    line = line.strip()
    letter, count = line.split('\t')

    if last_key == letter:
        occurance[letter] += int(count)
    else:
        occurance[letter] = 1
        last_key = letter

for key in occurance.keys():
    print('Letter: %s, Count: %s' % (key, occurance[key]))
