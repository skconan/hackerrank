#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#


def getTotalX(a, b):
    a = sorted(a)
    b = sorted(b)

    factor_of_b = []

    for i in range(a[-1], b[0] + 1):
        check = True
        for j in b:
            if not j % i == 0:
                check = False
        if check:
            factor_of_b.append(i)

    for i in factor_of_b.copy():
        for j in a:
            if not (i % j == 0) and i in factor_of_b:
                factor_of_b.remove(i)

    return len(factor_of_b)


if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    # f.write(str(total) + '\n')

    # f.close()
    print(total)
