n=int(input())
k=n
for i in range(1,n//2+2):
    print(' '*(i-1),end='')
    print('*'*k,end='')
    k=k-2
    print()
f=3
for i in range(1,n//2+1):
    print(' '*(n//2-i),end='')
    print('*'*f,end='')
    f=f+2
    print()
