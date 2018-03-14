#!/bin/python3

import sys


def birthdayCakeCandles(n, ar):
    ar = sorted(ar, reverse=True)
    ct = 1
    for i in ar[1:]:
        if i < ar[0]:
            break
        else:
            ct += 1
    return ct


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
