def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
            break
    return True
def nth_prime(x):
    num=3
    prime=2
    if x==1:
        return 2
    while(prime<x):
        num=num+2
        if (is_prime(num)):
            prime +=1
    return(num)
print(nth_prime(2))
print(nth_prime(3))
