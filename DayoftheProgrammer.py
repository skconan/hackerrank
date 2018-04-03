#!/bin/python3

import sys


def solve(year):
    dd = 256 - ((243 + (year <= 1917 and year % 4 == 0) +
                (year >= 1919 and (year % 400 == 0 or
                (year % 4 == 0 and not year % 100 == 0)))) - 
                13 * (year == 1918))
    mm = '09'
    return ('%02d' % dd) + '.' + mm + '.' + str(year)


year = int(input().strip())
result = solve(year)
print(result)
