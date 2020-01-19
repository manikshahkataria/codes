'''l=[0,'a',1,'b',1,'c',0]
ex=len(l)%3
le=len(l)
c=[]
if ex==2:
    for i in range(2,len(l),3):
        c.append(l[i])
        c.append(l[i-1])
        c.append(l[i-2])
    c.append(l[le-1])
    c.append(l[le-2])
elif ex==1:
    for i in range(2,len(l),3):
        c.append(l[i])
        c.append(l[i-1])
        c.append(l[i-2])
    c.append(l[le-1])
else:
    for i in range(2,len(l),3):
        c.append(l[i])
        c.append(l[i-1])
        c.append(l[i-2])
print(l)    
print(c)'''
    
    
n=input().split(' ')
k=int(input('rev by'))
le=len(n)
f=[]
ex=le%k
if ex==0:
    for i in range(k-1,le,k):
        c=0
        while(c<k):
            f.append(n[i-c])
            c=c+1
if ex!=0:
    for i in range(k-1,le,k):
        c=0
        while(c<k):
            f.append(n[i-c])
            c=c+1

    while(ex!=0):
        f.append(n[le-ex])
        ex=ex-1
        
    
print(n)
print(f)
            
