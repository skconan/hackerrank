#!/bin/python3

import sys


def migratoryBirds(n, ar):
    t = [0] * 6
    min = 6
    max = 0
    for i in ar:
        t[i] += 1
        if t[i] > max or (t[i] == max and i < min):
            min = i
            max = t[i]
    return min


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
