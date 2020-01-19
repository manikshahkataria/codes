def fact(n):
    f=1
    for i in range(n,1,-1):
        f=f*i
    return f
x=int(input('enter x'))
n=int(input('enter n'))
s=0
for i in range(1,2*n,2):
    s=s+(x**i/(fact(n)))
print(s)
