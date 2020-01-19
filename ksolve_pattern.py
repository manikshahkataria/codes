'''n=9
nha=n//2+1
for i in range(nha,0,-1):
    for k in range(nha-i):
        print(' ',end='')
    for j in range(i):
        print(str(i),end='')
        i=int(i)+1
    for p in range(i-2,nha-1,-1):
        print(str(p),end='')
        p=int(p)-1
    print()

n=9
i=n
nhalf=n//2+1
for i in range(i,0,-2):
    for k in range(0,(n-i)//2+1):
        print(' ',end='')
    for j in range((i+1)//2,i+1):
        print(j,end='')
    for p in range(i-1,(i+1)//2-1,-1):
        print(p,end='')
    print()
for i in range(1,n//2):
    for k in range(n//2-1,0,-1):
        print(' ',end='')
    
    for j in range(i+1,
    '''
n=9
nha=n//2+1
for i in range(nha,0-1):
    print(i)
    for k in range(nha-i):
        print(" ",end='')
    for j in range(n,0,-2):
        print(j,end='')
print()
