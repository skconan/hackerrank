#!/bin/python3

import sys

def miniMaxSum(arr):
    arr = sorted(arr)
    sum = 0
    for i in arr:
        sum += i
    print(sum-arr[-1], sum-arr[0])

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
