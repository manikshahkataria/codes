n=int(input('enter purchase value'))
d=n
if n<=5000:
    d=d-(d*.05)
    print('5% discount',d)
elif n<5000 and n>=10000:
    d=d-(d*.08)
    print('8% discount',d)
elif n<10000 and n>=25000:
    d=d-(d*.12)
    print('12% discount',d)
elif n<25000 and n>=50000:
    d=d-(d*.17)
    print('17% discount',d)
else :
    n>50000
    d=d-(d*.23)
    print('23% discount',d)
