lcm=1
a=int(input('enter 1st'))
b=int(input('entr se'))
i=2
while a!=1 and b!=1:
    if(a%i==0 and b%i==0):
        lcm=lcm*i
        a=a//i
        b=b//i

    elif a%i==0:
        lcm=lcm*i
        a=a//i
    elif b%i==0:
        lcm=lcm*i
        b=b//i
    else:
        i=i+1

lcm=lcm*a*b
print(lcm)
