#!/bin/python3

import sys


def solve(n, p):
    n = (n + (not n % 2 == 0) + 2 * (n % 2 == 0)) / 2
    p = (p + (not p % 2 == 0) + 2 * (p % 2 == 0)) / 2
    return int(min(p - 1, n - p))


n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
