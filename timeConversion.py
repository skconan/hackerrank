#!/bin/python3

import sys


def timeConversion(s):
    if (s[:2] != '12' and s[-2:] == 'PM') or (s[:2] == '12' and s[-2:] == 'AM'):
        hh = int(s[:2])
        hh += 12
        hh = hh if hh % 24 else 0
        return '%02d' % hh + s[2:-2]
    else:
        return s[:-2]


s = input().strip()
result = timeConversion(s)
print(result)
