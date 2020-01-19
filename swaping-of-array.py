a=[]

for i in range(0,12):
    x=int(input('enter the elements'))
    a.append(x)
b=len(a)
mid=b//2
print(mid)
for j in range(0,mid):
    for k in range(11,mid-1,-1):
        temp=a[j]
        a[j]=a[k]
        a[k]=temp
print(a)    

