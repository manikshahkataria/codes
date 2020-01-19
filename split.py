s=input('enter string')
a=s.split()
l=len(a)
print(l)
print(a)
i=0
while i<l:
    if i==l-1:
        print(a[i],end='')
    else:
        print(a[i][0],end='')
    i=i+1
