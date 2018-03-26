#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ct_a = 0
    ct_o = 0
    for i in apples:
        if i >=0 and s <= a + i <= t:
            ct_a += 1
    
    for i in oranges:
        if i <=0 and s <= b + i <= t:
            ct_o += 1

    print(ct_a)
    print(ct_o)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)
