#!/bin/python3

import sys

def staircase(n):
    for i in range(0,n):
        print('{0: >{1}}'.format('#'*(i+1),n))

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)