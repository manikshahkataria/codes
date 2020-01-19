n=int(input())
c=1
for i in range(1,n+2):
    for j in range(1,n+1):
        if(i!=1 and j==n//2+1):
            print(str(c),end='')
            c+=1
        else:
            print(n,end='')
    print()
    
