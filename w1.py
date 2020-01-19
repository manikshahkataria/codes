n=list(map(int,input().rstrip().split()))
l=(sum(n)-1)
f=int(n[0])
l=f+2
for i in range(1,5):
    for j in range(i):
        print(f,end='')
    f=f+1
    print()
for i in range(1,4):
    for j in range(3,i-1,-1):
        print(l,end='')
    l=l-1
    print()
