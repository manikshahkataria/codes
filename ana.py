import random
import math
s=input('enter string')
l1=[]
for i in s:
    l1.append(i)
i=1
lst=[]
lst.append(l1)

length=len(s)
n=math.factorial(length)
print(n)

while i<=n-1:
    l2=l1.copy()
    
    random.shuffle(l2)

    if lst.count(l2)==0:
        lst.append(l2.copy())
        i=i+1
print(lst)
for i in list(lst):
    
    k=(i[::-1])
    print(k)
    if (k==i):
        print('Anadrome')
    else:
        print('not Anadrome')
