#!/bin/python3

import sys

def diagonalDifference(a):
    b,c = 0,0
    len_a = len(a)
    rng = range(0,len_a)
    for i in rng:
        for j in rng:
            if i == j:
                b += a[i][j]
            if i == len_a - j -1:
                c += a[i][j]
    return abs(c-b)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
