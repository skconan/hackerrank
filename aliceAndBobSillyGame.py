#!/bin/python3

import sys
import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def numberOfPrime():
    num = [1, 2]
    ct = 2
    for i in range(3, 100001):
        if isPrime(i):
            ct += 1
        num.append(ct)
    return num


noPrime = numberOfPrime()
g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    if noPrime[n - 1] % 2 == 0:
        print('Alice')
    else:
        print('Bob')
