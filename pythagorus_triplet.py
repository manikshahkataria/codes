def pitr(n):
    n=int(n)
    if n>0:
        for a in range(1,n-1):
            for b in range(a+1,n):
                for c in range(b+1,n+1):
                    if a*a+b*b==c*c:
                        print(a,b,c)
    else:
        print("no triplet")
m=int(input('enter the range'))
d=m
pitr(d)
