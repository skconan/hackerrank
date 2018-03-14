#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    sum = 0
    for num in ar:
        sum += int(num)
    return sum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
