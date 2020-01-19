import math
up=int(input('enter upper limit'))
lo=int(input('enter lower limit'))
sumi=int(input('sum u want'))
prime=[]
pair=0
for i in range(2,up+1):
    prime.append(i)
i=2
while(i<=int(math.sqrt(up))):
    if i in prime:
        for j in range(i*2,up+1,i):
            if j in prime:
                prime.remove(j)
    i=i+1
print(prime)

p=[x for x in prime if x>=10 ]
print(p)
if sumi<p[0]:
    print('no pair possible')
else:
    for i in range(len(p)):
        j=i
        while(j<=len(p)-1):
            if (sumi==p[i]+p[j]):
                pair=pair+1
            j=j+1
            
print(pair)
    
