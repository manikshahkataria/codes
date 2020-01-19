n=int(input())
c=0
for i in range(1,n+1):
    if (i%2!=0):
        c=c+i
        for j in range(1,i+1):
            print(c,end='')
            c=c+1
            if (i!=j):
                print('*',end='')
    else:
        c=c+i-1
        for j in range(1,i+1):
            print(c,end='')
            c=c-1
            if (i!=j):
                print('*',end='')
    print()
            
        
