#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
#def diagonalDifference(arr):
  #  for i in range(n):
   #     s=s+arr[i][i]
    #print(s)



n = int(input('input'))


arr = []
l=0
r=0
d=0
for i in range(n):
    arr.append(list(map(int, input('dig').rstrip().split())))
for i in range(n):
    l=l+arr[i][i]
print(l)
for i in range(n):
    for j in range(n):
        if (i+j==n-1):
           r =r+arr[i][j]         
print(r)
d=r-l
print(abs(d))
    

#diagonalDifference()

