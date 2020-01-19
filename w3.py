n=int(input())
l=1
for i in range(1,n+1):
    k=1
    for j in range(0,i):
        print(l,end='')
        l=l+1
        if(k<i):
            print('*',end='')
            k=k+1
    print()

l=l-n   
for i in range(n,0,-1):
    for j in range(1,i+1):
        if(j<i):
            print(str(l)+'*',end='')
            l=l+1
        else:
            print(l,end='')
            l=l+1
    l=(l+1)-2*i
    
    print()
        

