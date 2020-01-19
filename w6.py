n=int(input())
k=0
f=1
b=n*n+1
for i in range(n):
    for j in range(k):
        print('-',end='')
    k=k+2
    

    for j in range(i+1,n+1):
        print(str(f)+"*",end='')
        f=f+1
    

    
    
    for j in (range(i+1,n)):
        print(str(b)+"*",end='')
        b=b+1
    print(b)
    b-=2*((n-i)-1)
    print()
    
    
