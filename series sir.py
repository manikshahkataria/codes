x=int(input('enter x'))
n =int(input('enter series'))
f=1
s=0
for i in range(1,n+1):
    p=x**i
    j=1
for j in range(i,0,-1):
        f=f*j
        s=s+p/j
        print(s)

