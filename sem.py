
n=int(input('enter the no'))
prime_factor=[]
prime=[]
for i in range(2,n+1):
    if (n%i==0):
        prime_factor.append(i)#it will give the factors of that no


for i in prime_factor:
    
    k=2
    
    while k<i:
        if i%k==0:
            break
        k+=1
    else:
        prime.append(i)#it will search all the prime no in b/w the factors
l=len(prime)

if l==1:
    print('this is semiprime')
    exit #if there is only one prime no then yes

else:
    result=1#if there is more than one prime no it will mul it if it is equal to n then yes
    for x in prime:
        result=result*x

    if (result==n):
        print('this is semiprime')
    else:
        print('not semiprime')
    


