#!/bin/python3

import sys


def appendAndDelete(s, t, k):
    same = 0
    for i in range(0, min(len(s), len(t))):
        if s[0:i + 1] == t[0:i + 1]:
            same += 1
        else:
            break
    rm = max(0, len(s) - len(t))
    add = max(0, len(t) - len(s))
    rm_add = (min(len(s), len(t)) - same) * 2
    k -= rm_add + rm + add

    if k < 0:
        return 'No'
    elif k == 0:
        return 'Yes'
    elif k % 2 == 0:
        return 'Yes'
    elif k > same * 2:
        return 'Yes'
    else:
        return 'No'


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
