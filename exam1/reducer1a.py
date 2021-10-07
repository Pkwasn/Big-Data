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

max_occur = {'max':('letter',0)}

for key in occurance.keys():
    letter, occur = max_occur['max']
    if occurance[key] > occur:
        max_occur['max'] = (key,occurance[key])

print(max_occur['max'])
