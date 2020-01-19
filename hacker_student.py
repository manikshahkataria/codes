
import os
import sys


n = int(input())

grades = []

for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)
print(grades)

for i in grades:
    if i>38:
        f=(int(i/10)*10)
        print(f)
        l=int(i%10)
        print(l)
        if l==3 or l==4 or l==5:
            i=f+5
            print(i)
        elif l==8 or l==9:
            i=f+10
            print(i)
        else:
            print(i)
    else:
        print(i)
