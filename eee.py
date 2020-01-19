def nth_prime_number(n):
    if n==1:
        return 2
    count = 1
    num = 3
    while(count <= n):
        if is_prime(num):
            count +=1
            if count == n:
               return num
        num +=2 #optimization

def is_prime(num):
    factor = 2
    while (factor < num):
        if num%factor == 0:
             return False
        factor +=1
    return True

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

    
n=int(input(""))


if n%2==0:
    print(nth_prime_number(n/2))
else:
    n=n//2+2
    
    print(fib(n))
