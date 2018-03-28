#!/bin/python3

import sys


def kangaroo(x1, v1, x2, v2):
    if v1 == 0 or v2 == 0 or v1 == v2:
        return 'NO'
    res = (x2 * v1 - x1 * v2) / ((v1 - v2) * 1.0)
    if res == int(res) and res >= 0 and res >= x1 and res >= x2 and (int(res) - x1) % v1 + (int(res) - x2) % v2 == 0:
        return 'YES'
    else:
        return 'NO'


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
