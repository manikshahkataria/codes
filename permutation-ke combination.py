string=input('enter string')
def permute(a,l,r):
    if (l==r):
        print(a)
    else:
        for i in range(l,r+1):
            a[i],a[1]=a[1],a[i]
            permute(a,l,r+1)
            a[i],a[1]=a[1],a[i]
n=len(string)
a=list(string)
permute(a,0,n-1)
