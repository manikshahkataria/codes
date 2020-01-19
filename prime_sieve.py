import math
n=int(input('enter the limit'))
prime=[]
for i in range(2,n+1):
    prime.append(i)
i=2
while(i<=int(math.sqrt(n))):
    if i in prime:
        for j in range(i*2,n+1,i):
            if j in prime:
                prime.remove(j)
    i=i+1
print(prime)
for i in prime:
    print(i,end=' ')
