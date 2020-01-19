n=int(input())
l=1

for i in range(1,n+1):
    k=1
    d=i%2
    r=l+i-1
    
    for j in range(i):
        if(d==0):
            print(r,end='')
            r=r-1
            if(k<i):
                print('*',end='')
                k=k+1
            l=l+1
            continue
        print(l,end='')
        l=l+1
        if(k<i):
            print('*',end='')
            k=k+1
    print()
