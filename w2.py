n=int(input())
for i in range(1,n+1):
    k=1
    for j in range(0,i):
        print(i,end='')
        if(k<i):
            print('*',end='')
            k=k+1
    print()
for i in range(n,0,-1):
    k=1
    for j in range(0,i):
        print(i,end='')
        if(k<i):
            print('*',end='')
            k=k+1
    print()
