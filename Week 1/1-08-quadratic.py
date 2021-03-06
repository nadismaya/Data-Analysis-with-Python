#!usr/bin/env python 3
import math


def solve_quadratic(a,b,c):
    x1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
    x2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
    return x1,x2


print(solve_quadratic(1,2,1))