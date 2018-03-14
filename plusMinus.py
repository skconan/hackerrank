#!/bin/python3

import sys


def plusMinus(arr):
    ct_p = 0
    ct_n = 0
    ct_z = 0

    for i in arr:
        if i > 0:
            ct_p += 1
        elif i < 0:
            ct_n += 1
        else:
            ct_z += 1

    ct = float(ct_p + ct_n + ct_z)
    print('%.6f' % (ct_p / ct))
    print('%.6f' % (ct_n / ct))
    print( '%.6f' % (ct_z / ct))


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
