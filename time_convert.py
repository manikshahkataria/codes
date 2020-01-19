#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    ampm=s[-2:]#get the time is in am or pm
    time=s[:-2].split(':')
    print(time)
    hour=time[0];minute=time[1];sec=time[2]#seting index of hr min sec
    print(hour)
    if ampm=='PM' and hour!='12':
        hour=int(hour)+12
    elif ampm=='AM'and hour=='12':
        hour='00'
    return'{}:{}:{}'.format(hour,minute,sec)#using arugs and kurgs
s = input()


result = timeConversion(s)

print(result)
