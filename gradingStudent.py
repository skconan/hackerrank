#!/bin/python3

import sys

def solve(grades):
    grade_res = []
    for g in grades:
        if g < 38:
            grade_res.append(g)
        elif (g+1)%5 == 0:
            grade_res.append(g+1)
        elif (g+2)%5 == 0:
            grade_res.append(g+2)
        else:
            grade_res.append(g)
    return grade_res

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


