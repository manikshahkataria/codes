def inser(l):
    for i in range(1,len(l)):
        current=l[i]
        pos=i
        while current<l[pos-1] and pos>0:
            l[pos]=l[pos-1]
            pos=pos-1
        l[pos]=current



l=list(map(int,input().split()))

inser(l)
print(l)
