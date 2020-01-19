n=int(input('enter'))
d=n
x=len(str(n))
result=0
while n>0:
    digit=int(n%10)
    result=result+(digit**x)
    n=int(n/10)
if d==result:
    print('amstrong')
    
else:
    print('not amstrong')
