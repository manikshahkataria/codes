n=int(input())
for i in range(1,n+1):
    c=i
    m=4
    for j in range(i):
        print(c,end=' ')
        
        c=c+m
        m=m-1
    print()




    
n=int(input())
for i in range(0,n):
    c=15-i
    
    p=c
    m=4
    for j in range(i+1):
        print(p,end=' ')
        p=p-m
        m=m-1
    
    print()
