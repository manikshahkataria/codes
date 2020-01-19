n=int(input('enter no'))
result=0
for i in range(1,n):
    if (n%i)==0:
        result=result+i
if (result==n):
    print('perfct no')
else:
    print('not perfect')
